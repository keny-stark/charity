from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView, \
    UpdateView, CreateView, FormView, View
from myapp.models import News, Application, AssistanceProvided
from myapp.forms import NewsForm, ApplicationForm, \
    ApplicationAdminForm, FullSearchForm, AssistanceProvidedForm
from django.contrib import messages


class ApplicationCreateView(CreateView):
    template_name = 'for_drf.html'
    model = Application
    form_class = ApplicationForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Ваша заявка на рассмотрении и с '
                                       'вами в скоре свяжутся для потверждения!')
        return response


class ApplicationView(ListView):
    context_object_name = 'application'
    model = Application
    template_name = 'application_view.html'
    paginate_by = 5
    paginate_orphans = 1
    ordering = ['created_at']


class AssistanceProvidedCreateView(CreateView):
    model = AssistanceProvided
    template_name = 'assistance/create.html'
    form_class = AssistanceProvidedForm

    def dispatch(self, request, *args, **kwargs):
        self.application = self.get_application()
        if self.application.is_archived:
            messages.error(self.request, 'нужно потвердить заявку')
            return redirect('application_one_view', pk=self.application.pk)
        return super().dispatch(request)

    def form_valid(self, form):
        self.object = self.application.application_in_assistance_provided.create(
            **form.cleaned_data
        )
        return redirect('application_one_view', pk=self.application.pk)

    def get_application(self):
        application_pk = self.kwargs.get('pk')
        return get_object_or_404(Application, pk=application_pk)


class ApplicationUpdateView(UpdateView):
    model = Application
    template_name = 'application_update.html'
    context_object_name = 'application'
    form_class = ApplicationAdminForm

    def get_success_url(self):
        return reverse('application_one_view', kwargs={'pk': self.object.pk})


class ApplicationDetailView(DetailView):
    template_name = 'application_view_one_app.html'
    model = Application

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     article = self.object
    #     context['form'] = AssistanceProvidedForm()
    #     comments = article.application_in_assistance_provided.order_by('created_at')
    #     self.paginate_comments_to_context(comments, context)
    #     return context

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['form'] = AssistanceProvidedForm()
        comments = context['application'].application_in_assistance_provided.order_by('-date')
        self.paginate_comments_to_context(comments, context)
        return context

    def paginate_comments_to_context(self, comments, context):
        paginator = Paginator(comments, 3, 0)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        context['paginator'] = paginator
        context['page_obj'] = page
        context['comments'] = page.object_list
        context['is_paginated'] = page.has_other_pages()


class ApplicationDeleteView(DeleteView):
    template_name = 'application_delete_view.html'
    model = Application
    context_object_name = 'application'
    success_url = reverse_lazy('application')


class IndexView(ListView):
    context_object_name = 'news'
    model = News
    template_name = 'index.html'
    paginate_by = 3
    paginate_orphans = 1
    ordering = ['-created_at']


class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = 'news'


class NewsCreateView(CreateView):
    template_name = 'news_create.html'
    model = News
    form_class = NewsForm
    success_url = reverse_lazy('index')


class NewsUpdateView(UpdateView):
    model = News
    template_name = 'news_update.html'
    success_url = reverse_lazy('index')
    fields = ('title', 'description', 'image')
    context_object_name = 'news'


class NewsDeleteView(DeleteView):
    template_name = 'news_delete.html'
    model = News
    context_object_name = 'news'
    success_url = reverse_lazy('index')


class ApplicationSearchView(FormView):
    template_name = 'search.html'
    form_class = FullSearchForm

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        area = form.cleaned_data.get('area')
        district = form.cleaned_data.get('district')
        city = form.cleaned_data.get('city')
        pregnant = form.cleaned_data.get('pregnant')
        status = form.cleaned_data.get('status')
        check = form.cleaned_data.get('check')
        query = Q()
        if check:
            query = query & self.get_query(form, check)
        if name:
            query = query & self.get_name_query(form, name)
        if area:
            query = query & self.get_area_query(form, area)
        if district:
            query = query & self.get_district_query(form, district)
        if city:
            query = query & self.get_city_query(form, city)
        if pregnant:
            query = query & self.get_pregnant_query(form, pregnant)
        if status:
            query = query & self.get_status_query(form, status)
        application = Application.objects.filter(query).distinct()
        context = self.get_context_data()
        context['application'] = application
        return self.render_to_response(context)

    def get_name_query(self, form, name):
        query = Q()
        in_title = form.cleaned_data.get('name')
        if in_title:
            query = query | Q(name__icontains=name)
        return query

    def get_status_query(self, form, status):
        query = Q()
        in_title = form.cleaned_data.get('status')
        if in_title:
            query = query | Q(status__icontains=status)
        return query

    def get_area_query(self, form, area):
        query = Q()
        in_title = form.cleaned_data.get('area')
        if in_title:
            query = query | Q(area__area__contains=area)
        return query

    def get_district_query(self, form, district):
        query = Q()
        in_title = form.cleaned_data.get('district')
        if in_title:
            query = query | Q(district__district__icontains=district)
        return query

    def get_city_query(self, form, city):
        query = Q()
        in_title = form.cleaned_data.get('city')
        if in_title:
            query = query | Q(city_or_village__city_or_village__icontains=city)
        return query

    def get_pregnant_query(self, form, pregnant):
        query = Q()
        in_title = form.cleaned_data.get('pregnant')
        if in_title:
            query = query | Q(pregnancy__icontains=pregnant)
        return query

    def get_query(self, form, check):
        query = Q()
        in_title = form.cleaned_data.get('check')
        if in_title:
            query = query | Q(application_in_assistance_provided=None)
        return query


class DeleteView(DeleteView):
    model = Application
    # context_object_name = 'application'
    success_url = reverse_lazy('application')

