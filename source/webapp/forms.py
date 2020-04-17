from django import forms
from webapp.models import News, Application
from django.core.exceptions import ValidationError


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


class FullSearchForm(forms.Form):
    name = forms.CharField(max_length=100, required=False, label="По имени")
    area = forms.ChoiceField(initial=True, required=False, label="По областям")
    district = forms.ChoiceField(initial=True, required=False, label="По райёнам")
    city = forms.ChoiceField(initial=True, required=False, label="По селам или городам")
    pregnant = forms.ChoiceField(initial=True, required=False, label="По беременным")

    def clean(self):
        super().clean()
        data = self.cleaned_data
        if data.get('text'):
            if not (data.get('name') or data.get('area')
                    or data.get('district') or data.get('city') or data.get('pregnant')):
                raise ValidationError(
                    'Не наедено',
                    code='name_search_criteria_empty'
                )

        return data
