from django.db import models

# Create your models here.
class Students(models.Model):
    first_name = models.CharField(max_length= 15,null=True,blank=True)
    last_name =models.CharField(max_length= 15,null=True,blank=True)
    birth =models.IntegerField(max_length= 15,null=True,blank=True)
    mobile_number =models.IntegerField(max_length= 15,null=True,blank=True)
    GENDER_TYPES =(
    (1,'Male'),
    (2,'Female'),
    (3,'Other'),
    )
    gender =models.IntegerField(
    choices = GENDER_TYPES,
    default =1)
    def __str__(self):
        return str(self.first_name)

class Orders(models.Model):
    oders_name = models.CharField(max_length=15,null=True,blank=True)
    oders_quantity = models.IntegerField(max_length=15,null=True,blank=True)
    oders_discount = models.IntegerField(max_length=15,null=True,blank=True)
    oders_address = models.TextField(max_length=15,null=True,blank=True)
    oders_place_at = models.TextField(max_length=15,null=True,blank=True)
    oders_time = models.TimeField(max_length=15,null=True,blank=True)

    def __str__(self):
        return str(self,StudentsAddress,)


class StudentsAddress(models.Model):
    students = models.ForeignKey(Students,on_delete=models.CASCADE,null=True)
    street_address = models.CharField(max_length=15,null=True,blank=True)
    house_number = models.IntegerField(max_length=15,null=True,blank=True)
    city = models.CharField(max_length=15,null=True,blank=True)
    state = models.CharField(max_length=15,null=True,blank=True)
    country = models.CharField(max_length=15,null=True,blank=True)
    pin_code= models.IntegerField(max_length=15,null=True,blank=True)

    def __str__(self):
        return str(self.street_address)