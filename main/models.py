from distutils.command.upload import upload
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=180)
    image = models.ImageField(upload_to="cat_img/", null=True)

    def __str__(self):
        return self.title


class Brand(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="cat_img/", null=True)

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField(max_length=180)
    color_code = models.CharField(max_length=180)

    def __str__(self):
        return self.title


class Size(models.Model):
    title = models.CharField(max_length=180)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="product_imgs/")
    slug = models.CharField(max_length=200)
    detail = models.TextField()
    specs = models.TextField()
    detail = models.PositiveIntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.title
