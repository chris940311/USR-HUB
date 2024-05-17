from .models import Content
from django.conf import settings

def site_content(request):
    try:
        content = Content.objects.first()  # 假設只有一個Content實例
    except Content.DoesNotExist:
        content = None
    return {
        'site_content': content,
        "MEDIA_URL" : settings.MEDIA_URL,
    }