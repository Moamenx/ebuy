from django.db import models
from django.contrib.auth.models import User, Permission
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator

class Package(models.Model):
    name = models.CharField(null=False, max_length=50)
    description = models.CharField(null=False, max_length=1000)
    short_description = models.CharField(null=False, max_length=70)
    price = models.FloatField(null=True)
    discounted_price = models.FloatField(null=False, default=0)
    discount_rate = models.PositiveIntegerField(null=False, default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    main_photo = models.FileField(null=False)
    amount = models.PositiveIntegerField(null=False, default=0)
    amount_sold = models.PositiveIntegerField(null=False, default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.discount_rate > 0:
            self.discounted_price = self.price - (self.price * self.discount_rate)
            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(null=False, max_length=50)
    photo = models.FileField(null=False)

    def __str__(self):
        return self.name

#    from = models.CharField(null=False, max_lenght=3)
#    to = models.CharField(null=False, max_lenght=3)
#    rate = models.(null=False)


class PackageProduct(models.Model):
    name = models.CharField(null=False, max_length=50)
    description = models.CharField(null=False, max_length=1000)
    package = models.ForeignKey('Package', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name


class HotNews(models.Model):
    news = models.CharField(null= False, max_length=150)

    def __str__(self):
        return self.news[:25]


class Product(models.Model):
    name = models.CharField(null=False, max_length=50)
    description = models.CharField(null=False, max_length=2000)
    short_description = models.CharField(null=False, max_length=70)
    price = models.FloatField(null=True)
    discount_rate = models.PositiveIntegerField(null=False, default=0)
    discounted_price = models.FloatField(null=False, default=0)
    amount = models.IntegerField(null=False, default=1)
    amount_sold = models.IntegerField(null=False, default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=False)
    photo = models.FileField(null=False)

    def __str__(self):
        return self.name

    def get_product_category(self):
        return self.category

    def save(self, *args, **kwargs):
        if self.discount_rate > 0:
            print(self.discount_rate)
            print(self.price)
            self.discounted_price = self.price - (self.price * (self.discount_rate/100))
            print(self.discounted_price)
            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)



class Comment(models.Model):
    comment = models.TextField(null=False, max_length=255, help_text="Your comment here")
    product = models.ForeignKey('Product', on_delete=models.CASCADE)


class ProductPhoto(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=False, related_name='images')
    photo = models.FileField(null=False)

    def __str__(self):
        return self.product.name


class PackagePhoto(models.Model):
    package = models.ForeignKey('Package', on_delete=models.CASCADE, null=False)
    photo = models.FileField(null=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone_number = models.CharField(max_length=17, blank=False)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    def __str__(self):
        return "%s's profile" % self.user


class Cart(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True)
    package = models.ForeignKey('Package',on_delete=models.CASCADE, null=True)
    price = models.FloatField(null=False)
    quantity = models.PositiveIntegerField(null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Currency(models.Model):
    rate = models.FloatField(null=False)
    from_currency = models.CharField(null=False, max_length=3)
    to_currency = models.CharField(null=False, max_length=3)
