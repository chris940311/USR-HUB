from django.shortcuts import render
from .models import Post

# Create your views here.
def detail(request):
    posts = Post.objects.all()
    # 構建一個包含每個 Post 及其相關 DetailContent 的列表
    post_details = []
    for post in posts:
        contents = post.contents.all()
        post_details.append({
            'post': post,
            'contents': contents
        })
    print()
    return render(request, "detail.html", {'post_details': post_details})