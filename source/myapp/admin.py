from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import News, District, Area, CityOrVillage, Application, AssistanceProvided


class AssistanceProvidedInline(admin.TabularInline):
    model = AssistanceProvided
    fields = ('description', 'date')
    extra = 1


class ApplicationAdmin(admin.ModelAdmin):
    inlines = (AssistanceProvidedInline, )


admin.site.register(Application, ApplicationAdmin)
admin.site.register(News)
admin.site.register(Area)
admin.site.register(District)
admin.site.register(CityOrVillage)
