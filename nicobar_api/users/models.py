from django.db import models

# Create your models here.
class UserData(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=250)
    contact_number = models.IntegerField()
    password = models.CharField(max_length=1000)
    email = models.EmailField(max_length=70)

    def __str__(self):
        return self.username