from django.db import models
from django.contrib.auth.models import User

QUOTE_NEW = 'new'
QUOTE_APPROVED = 'approved'
QUOTE_STATUS_CHOICES = (
    (QUOTE_NEW, 'Новая'),
    (QUOTE_APPROVED, 'Подтверждена')
)
QUOTE_YES = 'yes'
QUOTE_NO = 'no'
QUOTE_PREGNANCY_CHOICES = (
    (QUOTE_YES, 'да'),
    (QUOTE_NO, 'нет')
)

class News(models.Model):
    image = models.ImageField(null=False, blank=False, upload_to='image_from_user', verbose_name='image')
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Title')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Description')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Time created')


    def __str__(self):
        return self.title


class Application(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False, verbose_name='Name and Last Name')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Description')
    phone = models.CharField(max_length=20, null=False, blank=False, verbose_name='phone')
    area = models.ForeignKey('myapp.Area', related_name='area_in_application',
                             on_delete=models.PROTECT, verbose_name='Area')
    district = models.ForeignKey('myapp.District', related_name='district_in_application',
                                 on_delete=models.PROTECT, verbose_name='District')
    city_or_village = models.ForeignKey('myapp.CityOrVillage', related_name='city_or_village_in_application',
                                        on_delete=models.PROTECT, verbose_name='City or Village',
                                        blank=False, null=False)
    address = models.CharField(max_length=40, null=False, blank=False, verbose_name='address')
    status = models.CharField(max_length=20, choices=QUOTE_STATUS_CHOICES, default=QUOTE_NEW, verbose_name='status')
    pregnancy = models.CharField(max_length=20, choices=QUOTE_PREGNANCY_CHOICES,
                                 default=QUOTE_NO, verbose_name='pregnancy')
    weeks_of_pregnancy = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,
                                             verbose_name='number of weeks of pregnancy')
    notes = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Notes')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Time of add')

    def __str__(self):
        return self.name

    @property
    def is_active(self):
        return self.status == QUOTE_APPROVED

    @property
    def is_archived(self):
        return self.status == QUOTE_NEW


class AssistanceProvided(models.Model):
    description = models.TextField(max_length=2000, null=False, blank=False, verbose_name='Description')
    assistance_provided = models.ForeignKey('myapp.Application',
                                            related_name='application_in_assistance_provided',
                                            on_delete=models.CASCADE, verbose_name='assistance provided',
                                            blank=True, null=True)
    date = models.DateField(auto_now_add=True, verbose_name='date of add')


class Area(models.Model):
    area = models.CharField(max_length=40, null=False, blank=False, verbose_name='Type')

    def __str__(self):
        return self.area


class District(models.Model):
    district = models.CharField(max_length=40, null=False, blank=False, verbose_name='district')
    area = models.ForeignKey('myapp.Area', related_name='district_of_area',
                             on_delete=models.PROTECT, verbose_name='area')

    def __str__(self):
        return self.district


class CityOrVillage(models.Model):
    city_or_village = models.CharField(max_length=40, null=False, blank=False,
                                       verbose_name='city or village')
    district = models.ForeignKey('myapp.District', related_name='city_of_district',
                                 on_delete=models.PROTECT, verbose_name='district')

    def __str__(self):
        return self.city_or_village
