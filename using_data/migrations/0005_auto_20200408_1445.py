# Generated by Django 2.2.9 on 2020-04-08 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailsearchpromotions', '0002_capitalizeverbose'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtaillinkchecker', '0005_auto_20180922_1835'),
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('using_data', '0004_social_media'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toolspage',
            name='aboutsubpage_ptr',
        ),
        migrations.DeleteModel(
            name='ToolsIndexPage',
        ),
        migrations.DeleteModel(
            name='ToolsPage',
        ),
    ]
