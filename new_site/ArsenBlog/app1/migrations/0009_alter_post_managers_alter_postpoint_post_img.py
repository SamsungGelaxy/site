# Generated by Django 4.2.11 on 2024-04-07 07:12

import app1.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_alter_post_tag'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='post',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='postpoint',
            name='post_img',
            field=models.ImageField(blank=True, upload_to=app1.models.save_img, verbose_name='picture_point'),
        ),
    ]