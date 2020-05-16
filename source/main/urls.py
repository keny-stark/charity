"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from main import settings
from django.urls import path, include
from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api_v1.urls')),
    path('accounts/', include('accounts.urls')),
    path('application/', ApplicationView.as_view(), name='application'),
    path('application/<int:pk>/', ApplicationDetailView.as_view(), name='application_one_view'),
    path('application/<int:pk>/update/', ApplicationUpdateView.as_view(), name='application_update_view'),
    path('application/create/', ApplicationCreateView.as_view(), name='application_add'),
    path('application/<int:pk>/delete/', ApplicationDeleteView.as_view(), name='application_delete'),
    path('', IndexView.as_view(), name='index'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news'),
    path('news/add/', NewsCreateView.as_view(), name='news_add'),
    path('news/<int:pk>/edit/', NewsUpdateView.as_view(), name='update_news'),
    path('news/<int:pk>/delete/', NewsDeleteView.as_view(), name='delete_news'),
    path('application/search/', ApplicationSearchView.as_view(), name='application_search'),
    path('application/<int:pk>/add_assistance_provided/', AssistanceProvidedCreateView.as_view(),
         name='assistance_provided_create'),
    path('application/delete/', DeleteView.as_view(), name='delete_more')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

