# Generated by Django 4.0.5 on 2022-08-11 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_comments_options_alter_heading_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='comments_post',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='likes',
        ),
    ]
