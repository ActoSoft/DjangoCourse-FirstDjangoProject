from django.db import models

class Movie(models.Model): # Siempre hay que heredar de models.Model
    title = models.CharField(max_length=140)
    sinopsis = models.TextField(blank=True, null=True)
    duration = models.PositiveIntegerField()
    calif = models.PositiveIntegerField(default=5)
    gender = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# CREAR UN MODELO PARA UN ACTOR