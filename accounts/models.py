from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.contrib.auth.models import AbstractUser

class UserRegistration(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)  # Para controle de aprovação

    def __str__(self):
        return str(self.name) if self.name else "Nome não disponível" 


# models.py

class CustomUser(AbstractUser):
    __original_password = None

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Adicione um related_name exclusivo para o CustomUser
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permission_set',  # Adicione um related_name exclusivo para o CustomUser
        blank=True,
    )

    def save(self, *args, **kwargs):
        if self.pk is not None:
            original = CustomUser.objects.get(pk=self.pk)
            self.__original_password = original.password
        super().save(*args, **kwargs)