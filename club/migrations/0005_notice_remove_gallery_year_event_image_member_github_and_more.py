# Generated by Django 5.1.3 on 2025-04-07 09:14

import django.core.validators
import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0004_notice_alter_gallery_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('details', models.TextField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='notices/', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg', 'pdf', 'docx', 'doc'])])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Notice',
                'verbose_name_plural': 'Notices',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AlterField(
            model_name='event',
            name='details',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.FileField(null=True, upload_to='events/', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])]),
        ),
        migrations.AddField(
            model_name='member',
            name='github',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='year',
        ),
    ]
