from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='名前', max_length=100)
    description = models.TextField(verbose_name='詳細', blank=True)


class Example(models.Model):
    category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.CASCADE, blank=True, null=True)
    operation = models.CharField(verbose_name='操作', max_length=100)
    result = models.CharField(verbose_name='结果', max_length=100)
    description = models.TextField(verbose_name='詳細', blank=True)
