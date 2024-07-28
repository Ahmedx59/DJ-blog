from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    auth = models.ForeignKey(User , on_delete=models.CASCADE , related_name='post_user')
    title = models.CharField(max_length=200)
    discription = models.TextField(max_length=1000)
    created_at = models.DateField()
    active = models.BooleanField(default=False)
    image = models.ImageField(upload_to='posts/')


    def __str__(self):
        return self.title