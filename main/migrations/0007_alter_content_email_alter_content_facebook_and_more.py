# Generated by Django 5.0.6 on 2024-05-16 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_content_email_content_facebook_content_instagram_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='email',
            field=models.EmailField(blank=True, help_text='電子郵件地址', max_length=254),
        ),
        migrations.AlterField(
            model_name='content',
            name='facebook',
            field=models.URLField(blank=True, help_text='請輸入Facebook連結'),
        ),
        migrations.AlterField(
            model_name='content',
            name='instagram',
            field=models.URLField(blank=True, help_text='請輸入Instagram連結'),
        ),
        migrations.AlterField(
            model_name='content',
            name='tel',
            field=models.CharField(blank=True, help_text='電話號碼格式：09xx-xxx-xxx', max_length=10),
        ),
        migrations.AlterField(
            model_name='content',
            name='twitter',
            field=models.URLField(blank=True, help_text='請輸入Twitter連結'),
        ),
        migrations.AlterField(
            model_name='content',
            name='youtube',
            field=models.URLField(blank=True, help_text='請輸入YouTube連結'),
        ),
    ]
