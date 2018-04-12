from django.contrib import admin
from main.models import *
from django.contrib.auth.models import User
# Register your models here.
from main.models import Product, ProductPhoto


class InlineImage(admin.TabularInline):
    model = ProductPhoto


class ProductAdmin(admin.ModelAdmin):
    inlines = [InlineImage]
    list_per_page = 20


class InlineImagePackage(admin.TabularInline):
    model = PackagePhoto


class InlinePackageProduct(admin.TabularInline):
    model = PackageProduct


class PackageAdmin(admin.ModelAdmin):
    inlines = [InlineImagePackage, InlinePackageProduct]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Package, PackageAdmin)
admin.site.register(HotNews)
