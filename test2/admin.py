from itertools import product

from django.contrib import admin
from test2.models import NewsCategory, News
# Register your models here.
@admin.register(NewsCategory)
class NewsAdminModel(admin.ModelAdmin):
    search_fields = ["category_name","id","created_at"]
    list_filter = ["created_at"]
    list_display = ["id","category_name" ,"created_at"]
    ordering = ["-id"]

@admin.register(News)
class NewsAdminModel(admin.ModelAdmin):
    search_fields = ["news_name","id"]
    list_filter = ["created_ad"]
    list_display = ["id", "news_name", "news_cost"]
    ordering = ["-id"]
