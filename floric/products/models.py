from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    cat_img = models.ImageField(upload_to='images/', null=False, blank=False, default='images/logo.png')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=1000, null=False)
    description = models.CharField(max_length=5000, null=False)
    weight = models.CharField(max_length=1000, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    color = models.CharField(max_length=1000, null=True, blank=True)
    brand = models.CharField(max_length=1000, null=True, blank=True)
    price = models.FloatField(null=False)
    size = models.CharField(max_length=15, null=True, blank=True)
    posted_time = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
#
#
# class PostImage(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='images/', null=True, blank=False)
#
#     def __str__(self):
#         return self.post.category
#
#
# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     author_name = models.CharField(max_length=100, null=False, default='viewer')
#     comment_time = models.DateTimeField(default=timezone.now)
#     content = models.TextField(max_length=1000, null=False)
#
#     def __str__(self):
#         return self.post.category
