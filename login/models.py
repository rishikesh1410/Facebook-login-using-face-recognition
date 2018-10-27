from django.db import models

class user(models.Model) :
    name = models.CharField(max_length=250)
    image = models.CharField(max_length=500)
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)

    def __str__(self) :
         return self.name + ' --- ' + self.username
