from django.db import models
from colorful.fields import RGBColorField
from django.utils.translation import gettext_lazy as _

class Post(models.Model):
    title = models.CharField(max_length=10, verbose_name="大標題")

    class Meta:
        verbose_name = _("村落簡介")
        verbose_name_plural = _("村落簡介")

    def __str__(self):
        return self.title

class DetailContent(models.Model):
    post = models.ForeignKey(Post, related_name='contents', on_delete=models.CASCADE, verbose_name="新增段落")

    subTitle = models.CharField(max_length=10, blank=True, null=True, verbose_name="(選填)副標題")

    subTitle_color = RGBColorField(default='#000000', blank=True, null=True, verbose_name="(選填)副標題字體顏色", help_text="請輸入十六進制顏色代碼，例如：#FF5733")
    image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name="(選填)圖片")
    image_description = models.CharField(max_length=20, blank=True, null=True, verbose_name="(選填)圖片簡介")
    image_description_color = RGBColorField(default='#000000', blank=True, null=True, verbose_name="(選填)圖片介紹字體顏色", help_text="請輸入十六進制顏色代碼，例如：#FF5733")
    text = models.TextField(blank=True, null=True, verbose_name="(選填)內容段落")

    def __str__(self):
        return f"Content for {self.post.title}"
