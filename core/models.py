from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

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

class Document(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.owner.username})"
    

class DocumentShare(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    signataire = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    shared_at = models.DateTimeField(auto_now_add=True)
    signed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.document.title} → {self.signataire.username}"