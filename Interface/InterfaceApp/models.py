from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.models import BaseUserManager
# Create your models here.
class Tester(models.Model):
    title = models.CharField(max_length=233)
    content = models.TextField(blank=True)
    texter = models.CharField(max_length=233)

class DataPoint(models.Model):
    x = models.FloatField()
    y = models.FloatField()

    def __str__(self):
        return f"DataPoint ({self.x}, {self.y})"

class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)

class CustomUser(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    # Добавьте дополнительные поля, если необходимо

    objects = CustomUserManager()

    def __str__(self):
        return self.username