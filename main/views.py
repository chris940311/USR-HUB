from django.shortcuts import render
from .models import Content
def is_content_editor(user):
    return user.groups.filter(name='ContentEditors').exists()

def index(request):
    item = Content.objects.last()
    icon = item.icon_img
    web_title = item.web_title
    content = {
        "item" : item,
        "icon" : icon,
        "web_title" :web_title
    }
    return render(request, 'index.html', content)
