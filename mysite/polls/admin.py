from django.contrib import admin

from .models import Cart, Good, Profile

admin.site.register(Cart)
admin.site.register(Good)
admin.site.register(Profile)