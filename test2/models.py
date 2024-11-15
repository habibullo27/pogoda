from functools import update_wrapper

from django.db import models
from unicodedata import category


# Create your models here.
class NewsCategory(models.Model):
    category_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class News(models.Model):
    news_name = models.CharField(max_length=66)
    news_cost = models.FloatField()
    news_descr = models.TextField()
    news_image = models.FileField(upload_to="news_image")
    news_category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    created_ad = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.news_name

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
