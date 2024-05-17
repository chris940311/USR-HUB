from django.db import models
from django.utils.translation import gettext_lazy as _


class Content(models.Model):
    background_image = models.ImageField(upload_to='background')
    icon_img = models.ImageField(upload_to='icon', blank=True)
    web_title = models.CharField(max_length=10)
    title1 = models.CharField(max_length=200)
    title2 = models.CharField(max_length=200)
    title3 = models.CharField(max_length=200)
    title4 = models.CharField(max_length=200)

    email = models.EmailField(blank=True, help_text="電子郵件地址")
    tel = models.CharField(
        max_length=10, 
        help_text="電話號碼格式：09xx-xxx-xxx", 
        blank=True
    )
    facebook = models.URLField(
        max_length=200,
        help_text="請輸入Facebook連結",
        blank=True
    )
    twitter = models.URLField(
        max_length=200, 
        help_text="請輸入Twitter連結", 
        blank=True
    )
    instagram = models.URLField(
        max_length=200, 
        help_text="請輸入Instagram連結", 
        blank=True
    )
    youtube = models.URLField(
        max_length=200, 
        help_text="請輸入YouTube連結", 
        blank=True
    )

    class Meta:
        verbose_name = _("村落資訊")
        verbose_name_plural = _("村落基本資訊")

    def __str__(self):
        return f"Content {self.id}"
    
