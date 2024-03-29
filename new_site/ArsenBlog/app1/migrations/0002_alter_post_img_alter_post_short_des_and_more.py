# Generated by Django 5.0 on 2023-12-28 06:29

import app1.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(upload_to='pictures/', verbose_name='picture'),
        ),
        migrations.AlterField(
            model_name='post',
            name='short_des',
            field=models.CharField(max_length=255, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='postpoint',
            name='post_img',
            field=models.ImageField(upload_to=app1.models.save_img, verbose_name='picture_point'),
        ),
    ]
