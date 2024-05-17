from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.

class AddActivity(models.Model):
    # 假設應該有一些欄位，例如名稱（name）
    title = models.CharField(max_length=20, verbose_name="活動標題")

    host = models.CharField(max_length=20,verbose_name="活動主辦人")

    description = models.TextField(max_length=200, verbose_name="活動簡介")

    date = models.DateField(verbose_name="活動日期")

    
    class Meta:
        verbose_name = _("活動列表")
        verbose_name_plural = _("活動內容")
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("activity_detail", kwargs={"pk": self.pk})
