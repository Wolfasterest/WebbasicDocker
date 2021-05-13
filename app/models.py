from django.db import models

class app(models.Model):
    name = models.CharField(max_length=50)
    short = models.TextField(max_length=300)
    description = models.TextField()
    picture = models.ImageField()

    def __str__(self):
        return self.name
