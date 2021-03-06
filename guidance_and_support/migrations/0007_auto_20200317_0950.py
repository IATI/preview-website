# Generated by Django 2.2.9 on 2020-03-17 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtaillinkchecker', '0005_auto_20180922_1835'),
        ('wagtailsearchpromotions', '0002_capitalizeverbose'),
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('guidance_and_support', '0006_supportpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='knowledgebasepage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='knowledgebasepage',
            name='social_media_image',
        ),
        migrations.RemoveField(
            model_name='supportpage',
            name='contact_email',
        ),
        migrations.RemoveField(
            model_name='supportpage',
            name='contact_link_label',
        ),
        migrations.RemoveField(
            model_name='supportpage',
            name='contact_link_label_en',
        ),
        migrations.RemoveField(
            model_name='supportpage',
            name='contact_link_label_es',
        ),
        migrations.RemoveField(
            model_name='supportpage',
            name='contact_link_label_fr',
        ),
        migrations.RemoveField(
            model_name='supportpage',
            name='contact_link_label_pt',
        ),
        migrations.DeleteModel(
            name='KnowledgebaseIndexPage',
        ),
        migrations.DeleteModel(
            name='KnowledgebasePage',
        ),
    ]
