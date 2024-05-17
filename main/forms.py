# 在你的 app 的 forms.py 中

from django import forms
from .models import Content

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['background_image','icon_img', 'title1', 'title2', 'title3', 'title4']
