# Generated by Django 5.0.6 on 2024-05-16 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailcontent',
            name='subTitle',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='副標題'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=10, verbose_name='大標題'),
        ),
    ]
