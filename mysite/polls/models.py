from django.db import models

# Create your models here.

class Student(models.Model):
    matricule = models.IntegerField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.matricule}: {self.first_name}/{self.last_name}. "
