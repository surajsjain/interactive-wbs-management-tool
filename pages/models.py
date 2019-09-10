from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    level = models.IntegerField()
    ProfilePicture = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, default='photos/default.jpg')

    def __str__(self):
        return self.user.username
