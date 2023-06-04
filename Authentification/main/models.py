from django.db import models

class User(models.Model):
    First_name = models.CharField(max_length = 200)
    Last_name  = models.CharField(max_length = 200)

    def __str__(self):
        return f"name is {self.First_name}"

    

