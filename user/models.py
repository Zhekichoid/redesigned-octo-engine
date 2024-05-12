from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20, null=True)
    image = models.ImageField(default='avatar.jpg', upload_to='Profile_Images')

    def __str__(self) -> str:
        return f'{self.staff.username} - Profile'