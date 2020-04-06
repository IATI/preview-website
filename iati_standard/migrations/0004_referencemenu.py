# Generated by Django 2.2.9 on 2020-03-18 17:18

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iati_standard', '0003_auto_20200318_1328'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReferenceMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(help_text='Associated git release tag', max_length=255)),
                ('menu_json', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]
