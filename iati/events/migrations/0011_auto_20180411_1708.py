# Generated by Django 2.0.4 on 2018-04-11 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_auto_20180406_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventtype',
            name='name_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='eventtype',
            name='name_es',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='eventtype',
            name='name_fr',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='eventtype',
            name='name_pt',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
