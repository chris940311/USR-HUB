# Generated by Django 5.0.6 on 2024-05-17 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0004_alter_detailcontent_image_description_color_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': '村落簡介', 'verbose_name_plural': '村落簡介'},
        ),
    ]