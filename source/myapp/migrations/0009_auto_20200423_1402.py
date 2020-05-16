# Generated by Django 2.2.4 on 2020-04-23 14:02

from django.db import migrations, models
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20200423_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assistanceprovided',
            name='assistance_provided',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET(myapp.models.Application), related_name='application_in_assistance_provided', to='myapp.Application', verbose_name='assistance provided'),
        ),
    ]