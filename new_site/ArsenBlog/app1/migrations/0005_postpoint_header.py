# Generated by Django 4.2.9 on 2024-01-21 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_alter_post_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='postpoint',
            name='header',
            field=models.CharField(default='Title', max_length=30, verbose_name='Header'),
        ),
    ]
