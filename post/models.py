from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    discription = models.TextField(max_length=1000)
    created_at = models.DateField()
    active = models.BooleanField(default=False)


    def __str__(self):
        return self.title