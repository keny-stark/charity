from django.urls import path, include
from rest_framework import routers
from .views import ProjectViewSet, AreaViewSet, DistrictViewSet, CityViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'applic', ProjectViewSet)
router.register(r'area', AreaViewSet, basename='area')
router.register(r'district', DistrictViewSet, basename='district')
router.register(r'city', CityViewSet, basename='city')

app_name = 'api_v1'

urlpatterns = [
    path('', include(router.urls)),
]
