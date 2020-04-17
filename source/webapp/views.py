from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView, FormView
from webapp.models import News, Application
from webapp.forms import NewsForm, ApplicationForm, ApplicationAdminForm, FullSearchForm, SimpleSearchForm


class ApplicationCreateView(CreateView):
    template_name = 'application_create.html'
    model = Application
    form_class = ApplicationForm
    success_url = reverse_lazy('index')


class ApplicationView(ListView):
    context_object_name = 'application'
    model = Application
    template_name = 'application_view.html'
    ordering = ['-created_at']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.form = self.get_search_form()
        self.search_query = self.get_search_query()

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_query(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


class ApplicationUpdateView(UpdateView):
    model = Application
    template_name = 'application_update.html'
    success_url = reverse_lazy('index')
    context_object_name = 'application'
    form_class = ApplicationAdminForm


class ApplicationDetailView(DetailView):
    template_name = 'application_view_one_app.html'
    model = Application
    context_object_name = 'application'


class ApplicationDeleteView(DeleteView):
    template_name = 'application_delete_view.html'
    model = Application
    context_object_name = 'application'
    success_url = reverse_lazy('application')


class IndexView(ListView):
    context_object_name = 'news'
    model = News
    template_name = 'index.html'


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
        query = Q()
        if name:
            query = query & self.get_name_query(form, name)
        if area:
            query = query & self.get_name_query(form, area)
        if district:
            query = query & self.get_name_query(form, district)
        if city:
            query = query & self.get_name_query(form, city)
        if pregnant:
            query = query & self.get_name_query(form, pregnant)
        application = Application.objects.filter(query).distinct()
        context = self.get_context_data()
        context['application'] = application
        return self.render_to_response(context)

    def get_name_query(self, form, text):
        query = Q()
        in_title = form.cleaned_data.get('name')
        if in_title:
            query = query | Q(name__icontains=text)
        return query

    def get_area_query(self, form, area):
        query = Q()
        in_title = form.cleaned_data.get('area')
        if in_title:
            query = query | Q(area_in_application__area__icontains=area)
        return query

    def get_district_query(self, form, district):
        query = Q()
        in_title = form.cleaned_data.get('district')
        if in_title:
            query = query | Q(district_in_application__district__icontains=district)
        return query

    def get_city_query(self, form, city):
        query = Q()
        in_title = form.cleaned_data.get('city')
        if in_title:
            query = query | Q(city_or_village_in_application__city_or_village__icontains=city)
        return query

    def get_pregnant_query(self, form, pregnant):
        query = Q()
        in_title = form.cleaned_data.get('pregnant')
        if in_title:
            query = query | Q(pregnancy__icontains=pregnant)
        return query
