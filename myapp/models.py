from django.db import models
# import uuid

class Contactus(models.Model):
    msg_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=50,default="")
    lname = models.CharField(max_length=50,default="")
    name = models.CharField(max_length=50,default="")
    email = models.CharField(max_length=70, default="")
    message = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name


