from distutils.command.upload import upload
from operator import mod
from statistics import mode
from tkinter import CASCADE
from unicodedata import category
from django.db import models
from django.core.validators import RegexValidator
from ckeditor_uploader.fields import RichTextUploadingField


# This is the category model


class Category(models.Model):
    category_name = models.CharField(
        default="", max_length=50, verbose_name="Name of Category")
    category_summary = models.CharField(
        default="", max_length=150, verbose_name="Something About The Range Of Products")
    category_card_image = models.ImageField(upload_to='category_card_images')
    category_herosection_image = models.ImageField(
        upload_to='category_card_images', default='/static/images/ship.webp')

    def __str__(self):
        return self.category_name


# This is the product model
class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default='')
    product_name = models.CharField(
        default="", max_length=50, verbose_name="Name of Product")
    product_summary = models.CharField(
        default="", max_length=150, verbose_name="Something About The Products")
    product_card_image = models.ImageField(upload_to='product_card_images')
    product_herosection_image = models.ImageField(
        upload_to='product_card_images', default='/static/images/ship.webp')
    product_info_body = RichTextUploadingField(default='')

    def __str__(self):
        return self.product_name

# This is the contact us model for quesries


class Query(models.Model):
    full_name = models.CharField(
        max_length=50, verbose_name="Full Name", default="")
    email = models.CharField(max_length=50, verbose_name="EMail")
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(
        validators=[phoneNumberRegex], max_length=12, unique=True)
    message = models.CharField(
        max_length=1000, verbose_name="Write A Message Here", default="")

    def __str__(self):
        return self.full_name


class HomeQuery(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
