from django.db import models
from django.contrib.auth.models import Group, AbstractUser
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=10)
    profile_img = models.ImageField(upload_to="profile_img/", null=True, blank=True)
    hostel_name = models.CharField(max_length=100, null=True, blank=True)
    room_number = models.CharField(max_length=2, null=True, blank=True)
