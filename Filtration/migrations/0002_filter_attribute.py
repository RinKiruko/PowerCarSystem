# Generated by Django 2.1.7 on 2019-04-03 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Catalog', '0002_auto_20190403_0932'),
        ('Filtration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filter',
            name='Attribute',
            field=models.OneToOneField(help_text='Характеристика для которой создается фильтр', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='filter', to='Catalog.Attribute', verbose_name='Характеристика товара'),
        ),
    ]
