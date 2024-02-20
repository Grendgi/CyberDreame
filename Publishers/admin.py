from django.contrib import admin
from .models import News, Category, NewsImage, NewsVideo, NewsFile, Comment

admin.site.register(News)
admin.site.register(Category)
admin.site.register(NewsImage)
admin.site.register(NewsVideo)
admin.site.register(NewsFile)
admin.site.register(Comment)
