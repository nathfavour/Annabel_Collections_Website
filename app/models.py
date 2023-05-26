"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.


class Products(models.Model):
    user = models.ForeignKey( User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length = 225, default = 'product name')
    image = models.ImageField()
    description = models.TextField()
    price = models.IntegerField(default = 0)
    ticked = models.BooleanField(default = False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Products, self).save()

    # Edit the detail function and change all occurences of 'id' into ''slug'.
    # A.category.A_set.all

    class Meta:
        order_with_respect_to = 'user'

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Products)


    