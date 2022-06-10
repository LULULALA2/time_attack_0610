from django.db import models

# Create your models here.
class User(models.Model):
    class Meta:
        db_table = "my_user"
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)