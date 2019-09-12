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

class UserPermissions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username + ' - ' + self.products

class UserAurhority(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.IntegerField()

    def __str__(self):
        return self.user.username + ' - ' + str(self.action)
