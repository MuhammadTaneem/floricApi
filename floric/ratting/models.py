from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
import sys

sys.path.append("..")
from products.models import Product


class Ratting(models.Model):
    star = models.IntegerField(null=False, blank=False, default=0)
    comment = models.CharField(max_length=1024, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name
