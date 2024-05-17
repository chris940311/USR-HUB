from django.contrib import admin
from .models import Post, DetailContent

class DetailContentInline(admin.StackedInline):
    model = DetailContent
    extra = 1
    verbose_name = "內容段落"
    verbose_name_plural = "內容段落"

    fieldsets = (
        (None, {
            'fields': ('post', 'subTitle', 'subTitle_color', 'image', 'image_description', 'image_description_color', 'text'),
        }),
    )

class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title',),
            'description': "請輸入大標題",
        }),
    )
    inlines = [DetailContentInline]
    list_display = ('title',)
    search_fields = ('title',)

admin.site.register(Post, PostAdmin)
