from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.TextField()
    genre = models.CharField(max_length=10)

    def __str__(self):
        res = f"{self.id}번째 영화 - {self.title}({self.genre})"
        return res