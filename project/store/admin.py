from .models import Category, Product
from django.contrib import admin

@admin.register(Category)
# This decorator introduces the model class to Django admin panel and we can define ModelAdmin classes in it.
# So we don't need use "admin.register.site(Model, ModelAdmin)" to introduce the model to the admin panel and define its ModelAdmin class separatly.
# Infact, it's a "syntactic sugar".
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    # "search_fields" creates a search bar in admin panel and makes the admin able to search for the model objects by spacified properties.
    # In this class, the admin can search for categories by their titles.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'registration_date']
    list_filter = ['category', 'registration_date']
    # "list_filter" adds a filter column in the admin panel which is used for filtering the model objects by spacified properties.
    ordering = ['-registration_date']
    # "ordering" sorts the model objects in the admin panel by spacified properties.
    # "-", which is written before the name of the property, makes the order descending. That means from the newest objects to the older ones.
    # By default, the order is ascending. That means from the oldest objects to the newer ones.
    readonly_fields = ['registration_date']
    # "readonly_fields" spacifies the properties which cannot be changed or edited by admin.
    search_fields = ['title', 'details']
