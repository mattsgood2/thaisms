from django.db import models

# Create your models here.
class YourAddress(models.Model):
    your_address = models.CharField(max_length=200)
    post_code = models.CharField(max_length=10)
    
