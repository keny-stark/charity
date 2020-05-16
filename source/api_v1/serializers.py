from rest_framework import serializers
from myapp.models import Application, Area, District, CityOrVillage


class CityOrVillageSerializer(serializers.HyperlinkedModelSerializer):
    district = serializers.PrimaryKeyRelatedField(queryset=District.objects.all())
    class Meta:
        model = CityOrVillage
        fields = ('id', 'city_or_village', 'district')


class DistrictSerializer(serializers.HyperlinkedModelSerializer):
    city = CityOrVillageSerializer(many=True, read_only=True)
    area = serializers.PrimaryKeyRelatedField(queryset=Area.objects.all())
    class Meta:
        model = District
        fields = ('id', 'district', 'area', 'city')


class AreaSerializer(serializers.HyperlinkedModelSerializer):
    district = DistrictSerializer(many=True, read_only=True)
    # area = serializers.PrimaryKeyRelatedField(queryset=Area.objects.all())
    class Meta:
        model = Area
        fields = ('id', 'area', 'district')


class ProjectSerializer(serializers.ModelSerializer):
    # area = AreaSerializer(many=True, read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Application
        fields = ('id', 'name', 'description', 'area', 'district', 'city_or_village', 'created_at')



