from django.db import models
from django import forms

# Create your models here.
class UserData(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    contact_number = models.IntegerField()
    password = models.CharField(max_length=1000)
    email = models.EmailField(max_length=70)

class ViewUser(forms.Form):
    username = forms.CharField(max_length=250)
    password = forms.PasswordInput()

    def clean_message(self):
        username = self.cleaned_data.get("username")
        dbuser = UserData.objects.filter(name=username)

        if not dbuser:
            raise forms.ValidationError("User does not exist in our db!")
        return username