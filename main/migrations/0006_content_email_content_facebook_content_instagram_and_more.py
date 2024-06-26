# Generated by Django 5.0.6 on 2024-05-15 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_content_background_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='content',
            name='facebook',
            field=models.CharField(blank=True, help_text='請輸入連結', max_length=200),
        ),
        migrations.AddField(
            model_name='content',
            name='instagram',
            field=models.CharField(blank=True, help_text='請輸入連結', max_length=200),
        ),
        migrations.AddField(
            model_name='content',
            name='tel',
            field=models.CharField(blank=True, help_text='09xx-xxx-xxx', max_length=10),
        ),
        migrations.AddField(
            model_name='content',
            name='twitter',
            field=models.CharField(blank=True, help_text='請輸入連結', max_length=200),
        ),
        migrations.AddField(
            model_name='content',
            name='youtube',
            field=models.CharField(blank=True, help_text='請輸入連結', max_length=200),
        ),
    ]
