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
    




class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name='user_comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE , related_name='post_comment')
    content = models.TextField(max_length=1000)
    created_at = models.DateField(auto_now_add=True)


    def __str__(self):
        return str(self.post)
