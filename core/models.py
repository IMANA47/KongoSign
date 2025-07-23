from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('ADMIN', 'Administrateur'),
        ('CLIENT', 'Client'),
        ('SIGNATAIRE', 'Signataire'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='CLIENT')

    def is_admin(self):
        return self.role == 'ADMIN'

    def is_client(self):
        return self.role == 'CLIENT'

    def is_signataire(self):
        return self.role == 'SIGNATAIRE'

    def __str__(self):
        return f"{self.username} ({self.role})"
