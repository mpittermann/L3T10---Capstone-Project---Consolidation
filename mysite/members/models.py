from django.db import models

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=50)
    id_number = models.CharField(max_length=20, primary_key=True)
    dob = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return (self.first_name + ' ' + self.last_name)