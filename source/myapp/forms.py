from django import forms
from myapp.models import News, Application, QUOTE_PREGNANCY_CHOICES,\
    Area, District, CityOrVillage, AssistanceProvided, QUOTE_STATUS_CHOICES
from django.core.exceptions import ValidationError


class AssistanceProvidedForm(forms.ModelForm):
    class Meta:
        model = AssistanceProvided
        fields = ['description']


class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        exclude = ['created_at']


class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        exclude = ['created_at', 'notes', 'status']


class ApplicationAdminForm(forms.ModelForm):

    class Meta:
        model = Application
        exclude = ['created_at']


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")


blank_choice = (('', '--- Выберите значение ---'),)


class FullSearchForm(forms.Form):
    name = forms.CharField(max_length=100, required=False, label="По имени")
    area = forms.ModelChoiceField(queryset=Area.objects.all(), initial=True, required=False, label="По областям")
    district = forms.ModelChoiceField(queryset=District.objects.all(), initial=True, required=False, label="По райёнам")
    city = forms.CharField(required=False, label="По селам или городам")
    pregnant = forms.ChoiceField(choices=blank_choice + QUOTE_PREGNANCY_CHOICES, initial=True,
                                 required=False, label="По беременным")
    status = forms.ChoiceField(choices=blank_choice + QUOTE_STATUS_CHOICES, initial=True, required=False, label="статус")
    check = forms.BooleanField(initial=True, required=False, label="кому еще не было помощи")

    def clean(self):
        super().clean()
        data = self.cleaned_data
        if data.get('name'):
            if not (data.get('name') or data.get('area')
                    or data.get('district') or data.get('city') or data.get('pregnant')):
                raise ValidationError(
                    'Не наедено',
                    code='name_search_criteria_empty'
                )

        return data
