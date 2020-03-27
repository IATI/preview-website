# Generated by Django 2.2.9 on 2020-02-25 14:49

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('get_involved', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='getinvolveditems',
            name='description_en',
            field=wagtail.core.fields.RichTextField(help_text='Description for the item', null=True),
        ),
        migrations.AddField(
            model_name='getinvolveditems',
            name='description_es',
            field=wagtail.core.fields.RichTextField(help_text='Description for the item', null=True),
        ),
        migrations.AddField(
            model_name='getinvolveditems',
            name='description_fr',
            field=wagtail.core.fields.RichTextField(help_text='Description for the item', null=True),
        ),
        migrations.AddField(
            model_name='getinvolveditems',
            name='description_pt',
            field=wagtail.core.fields.RichTextField(help_text='Description for the item', null=True),
        ),
        migrations.AddField(
            model_name='getinvolveditems',
            name='link_label_en',
            field=models.CharField(blank=True, help_text='Optional: link label for the item', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='getinvolveditems',
            name='link_label_es',
            field=models.CharField(blank=True, help_text='Optional: link label for the item', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='getinvolveditems',
            name='link_label_fr',
            field=models.CharField(blank=True, help_text='Optional: link label for the item', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='getinvolveditems',
            name='link_label_pt',
            field=models.CharField(blank=True, help_text='Optional: link label for the item', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='getinvolveditems',
            name='title_en',
            field=models.CharField(help_text='Title for the item', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='getinvolveditems',
            name='title_es',
            field=models.CharField(help_text='Title for the item', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='getinvolveditems',
            name='title_fr',
            field=models.CharField(help_text='Title for the item', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='getinvolveditems',
            name='title_pt',
            field=models.CharField(help_text='Title for the item', max_length=255, null=True),
        ),
    ]
