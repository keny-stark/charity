# Generated by Django 2.2.4 on 2020-04-23 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20200423_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assistanceprovided',
            name='assistance_provided',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET, related_name='application_in_assistance_provided', to='myapp.Application', verbose_name='assistance provided'),
        ),
    ]
