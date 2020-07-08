from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
    user = models.ForeignKey(User, related_name='addresses', on_delete=models.CASCADE)
    street = models.CharField(max_length=140)
    exterior_number = models.PositiveIntegerField()
    internal_number = models.PositiveIntegerField(blank=True, null=True)
    colony = models.CharField(max_length=100)
    city = models.CharField(max_length=140)
    state = models.CharField(max_length=140)
    coutry = models.CharField(max_length=140)
    postal_code = models.CharField(max_length=6)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Dirección #{self.id} del usuario {self.user.first_name} {self.user.last_name}'