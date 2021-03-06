# Generated by Django 2.1.7 on 2019-04-03 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catalog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GoodAttribute',
            new_name='Attribute',
        ),
        migrations.RemoveField(
            model_name='category',
            name='TranslitTitle',
        ),
        migrations.AddField(
            model_name='good',
            name='PublishedDate',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='good',
            name='State',
            field=models.CharField(choices=[('Stock', 'Есть в наличии'), ('Sold', 'Продано')], max_length=50, null=True, verbose_name='Наличиe:'),
        ),
        migrations.AlterField(
            model_name='categorygroup',
            name='Title',
            field=models.CharField(max_length=50, null=True, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='good',
            name='UrlHash',
            field=models.CharField(max_length=70, null=True, unique=True),
        ),
    ]
