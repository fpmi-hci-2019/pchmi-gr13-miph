import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Good(models.Model):
    good_name = models.CharField(max_length=30)
    good_description = models.CharField(max_length=300)
    good_image = models.URLField()
    good_price = models.FloatField()

    def __str__(self):
        return self.good_name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    good = models.ForeignKey(Good, on_delete=models.SET_NULL, null=True, blank=True)
    order_date = models.DateTimeField()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_image = models.URLField()
    user_cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()