# Generated by Django 2.2.4 on 2020-04-23 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20200423_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assistanceprovided',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='date of add'),
        ),
    ]
