from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'admin', 'Administrador'
        ATTENDANT = 'attendant', 'Atendente'
        CLIENT = 'client', 'Cliente'

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.CLIENT,
    )

    def __str__(self):
        return f'{self.username} ({self.get_role_display()})'

    @property
    def is_admin(self):
        return self.role == self.Role.ADMIN

    @property
    def is_attendant(self):
        return self.role == self.Role.ATTENDANT

    @property
    def is_client(self):
        return self.role == self.Role.CLIENT