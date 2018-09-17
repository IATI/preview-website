# Generated by Django 2.0.5 on 2018-09-17 11:24

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20180626_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peoplepage',
            name='profile_content_editor',
            field=wagtail.core.fields.StreamField((('section_heading', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('paragraph', wagtail.core.blocks.CharBlock(icon='pilcrow')), ('pullquote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock('quote title')),))), ('profile_editor', wagtail.core.blocks.StructBlock((('name', wagtail.core.blocks.CharBlock(max_length=100, required=False)), ('profile_picture', wagtail.images.blocks.ImageChooserBlock(icon='image', label='Profile picture', required=False)), ('organisation_logo', wagtail.images.blocks.ImageChooserBlock(icon='image', label='Organisation logo', required=False)), ('organisation_name', wagtail.core.blocks.CharBlock(max_length=100, required=False)), ('IATI_role', wagtail.core.blocks.CharBlock(max_length=100, required=False)), ('external_role', wagtail.core.blocks.CharBlock(max_length=200, required=False)), ('description', wagtail.core.blocks.TextBlock(required=False)), ('IATI_constituency', wagtail.core.blocks.CharBlock(max_length=200, required=False))), icon='image'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='peoplepage',
            name='profile_content_editor_en',
            field=wagtail.core.fields.StreamField((('section_heading', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('paragraph', wagtail.core.blocks.CharBlock(icon='pilcrow')), ('pullquote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock('quote title')),))), ('profile_editor', wagtail.core.blocks.StructBlock((('name', wagtail.core.blocks.CharBlock(max_length=100, required=False)), ('profile_picture', wagtail.images.blocks.ImageChooserBlock(icon='image', label='Profile picture', required=False)), ('organisation_logo', wagtail.images.blocks.ImageChooserBlock(icon='image', label='Organisation logo', required=False)), ('organisation_name', wagtail.core.blocks.CharBlock(max_length=100, required=False)), ('IATI_role', wagtail.core.blocks.CharBlock(max_length=100, required=False)), ('external_role', wagtail.core.blocks.CharBlock(max_length=200, required=False)), ('description', wagtail.core.blocks.TextBlock(required=False)), ('IATI_constituency', wagtail.core.blocks.CharBlock(max_length=200, required=False))), icon='image'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='peoplepage',
            name='profile_content_editor_es',
            field=wagtail.core.fields.StreamField((('section_heading', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('paragraph', wagtail.core.blocks.CharBlock(icon='pilcrow')), ('pullquote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock('quote title')),))), ('profile_editor', wagtail.core.blocks.StructBlock((('name', wagtail.core.blocks.CharBlock(max_length=100, required=False)), ('profile_picture', wagtail.images.blocks.ImageChooserBlock(icon='image', label='Profile picture', required=False)), ('organisation_logo', wagtail.images.blocks.ImageChooserBlock(icon='image', label='Organisation logo', required=False)), ('organisation_name', wagtail.core.blocks.CharBlock(max_length=100, required=False)), ('IATI_role', wagtail.core.blocks.CharBlock(max_length=100, required=False)), ('external_role', wagtail.core.blocks.CharBlock(max_length=200, required=False)), ('description', wagtail.core.blocks.TextBlock(required=False)), ('IATI_constituency', wagtail.core.blocks.CharBlock(max_length=200, required=False))), icon='image'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='peoplepage',
            name='profile_content_editor_fr',
            field=wagtail.core.fields.StreamField((('section_heading', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('paragraph', wagtail.core.blocks.CharBlock(icon='pilcrow')), ('pullquote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock('quote title')),))), ('profile_editor', wagtail.core.blocks.StructBlock((('name', wagtail.core.blocks.CharBlock(max_length=100, required=False)), ('profile_picture', wagtail.images.blocks.ImageChooserBlock(icon='image', label='Profile picture', required=False)), ('organisation_logo', wagtail.images.blocks.ImageChooserBlock(icon='image', label='Organisation logo', required=False)), ('organisation_name', wagtail.core.blocks.CharBlock(max_length=100, required=False)), ('IATI_role', wagtail.core.blocks.CharBlock(max_length=100, required=False)), ('external_role', wagtail.core.blocks.CharBlock(max_length=200, required=False)), ('description', wagtail.core.blocks.TextBlock(required=False)), ('IATI_constituency', wagtail.core.blocks.CharBlock(max_length=200, required=False))), icon='image'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='peoplepage',
            name='profile_content_editor_pt',
            field=wagtail.core.fields.StreamField((('section_heading', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('paragraph', wagtail.core.blocks.CharBlock(icon='pilcrow')), ('pullquote', wagtail.core.blocks.StructBlock((('quote', wagtail.core.blocks.TextBlock('quote title')),))), ('profile_editor', wagtail.core.blocks.StructBlock((('name', wagtail.core.blocks.CharBlock(max_length=100, required=False)), ('profile_picture', wagtail.images.blocks.ImageChooserBlock(icon='image', label='Profile picture', required=False)), ('organisation_logo', wagtail.images.blocks.ImageChooserBlock(icon='image', label='Organisation logo', required=False)), ('organisation_name', wagtail.core.blocks.CharBlock(max_length=100, required=False)), ('IATI_role', wagtail.core.blocks.CharBlock(max_length=100, required=False)), ('external_role', wagtail.core.blocks.CharBlock(max_length=200, required=False)), ('description', wagtail.core.blocks.TextBlock(required=False)), ('IATI_constituency', wagtail.core.blocks.CharBlock(max_length=200, required=False))), icon='image'))), blank=True, null=True),
        ),
    ]
