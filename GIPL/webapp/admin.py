from django.contrib import admin
from webapp.models import Category, Product, Query, HomeQuery

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Query)
admin.site.register(HomeQuery)
