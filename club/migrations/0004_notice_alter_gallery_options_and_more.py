# Generated by Django 5.1.3 on 2025-04-07 09:05

import datetime
import django.core.validators
import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0003_contactrequest_event'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'ordering': ['-event_date'], 'verbose_name': 'Gallery', 'verbose_name_plural': 'Gallery'},
        ),
        migrations.AddField(
            model_name='gallery',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='gallery',
            name='event_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='gallery',
            name='year',
            field=models.IntegerField(default=2025),
            preserve_default=False,
        ),
    ]
