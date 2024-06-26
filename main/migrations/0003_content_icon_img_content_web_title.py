# Generated by Django 5.0.6 on 2024-05-15 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_content_delete_index_delete_indextitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='icon_img',
            field=models.ImageField(default='Default description', upload_to='image/icon'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='content',
            name='web_title',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
