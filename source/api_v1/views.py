from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import ProjectSerializer, AreaSerializer, CityOrVillageSerializer, DistrictSerializer
from myapp.models import Application, Area, District, CityOrVillage


class CityViewSet(viewsets.ModelViewSet):
    model = CityOrVillage
    serializer_class = CityOrVillageSerializer

    def get_queryset(self):
        queryset = CityOrVillage.objects.all()
        district = self.request.query_params.get('district')

        if district:
            queryset = queryset.filter(district=district)
        return queryset


class DistrictViewSet(viewsets.ModelViewSet):
    model = District
    serializer_class = DistrictSerializer

    def get_queryset(self):
        queryset = District.objects.all()
        area = self.request.query_params.get('area')

        if area:
            queryset = queryset.filter(area=area)
        return queryset


class AreaViewSet(viewsets.ModelViewSet):
    model = Area
    serializer_class = AreaSerializer

    def get_queryset(self):
        queryset = Area.objects.all()
        return queryset


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = ProjectSerializer
    queryset = Application.objects.all()
