# Generated by Django 5.1.3 on 2025-04-07 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0005_notice_remove_gallery_year_event_image_member_github_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='panelmember',
            options={'ordering': ['category', 'ordering'], 'verbose_name': 'Panel Member', 'verbose_name_plural': 'Panel Members'},
        ),
        migrations.AddField(
            model_name='panelmember',
            name='category',
            field=models.CharField(choices=[('panel', 'Panel Member'), ('teachers', 'Teachers Advisory Panel'), ('alumni', 'Alumni Advisory Panel')], default='panel', max_length=20),
        ),
    ]
