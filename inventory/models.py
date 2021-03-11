from django.db import models
from django.contrib.auth.models import User

class Management(models.Model):
    product_name = models.CharField(max_length=128)
    purity = models.CharField(max_length=32)
    quantity = models.IntegerField()
    residual_quantity = models.IntegerField()
    manufacturer = models.CharField(max_length=32)
    storage_location = models.CharField(max_length=32)
    category = models.CharField(max_length=32)
    partname = models.CharField(max_length=32)
    division = models.CharField(max_length=32)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    registration_date = models.DateField()
    xpiration_date = models.DateField()
    comment = models.CharField(max_length=128, null=True, blank=True)
    msds = models.FileField(blank=True, null=True, upload_to='files/') 
    modify_date = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.product_name


class Question(models.Model):
    item_code = models.IntegerField()
    product_name = models.CharField(max_length=64)
    manufacturer = models.CharField(max_length=64)
    storage_location = models.CharField(max_length=64)
    team_name = models.CharField(max_length=16)
    quantity = models.IntegerField()
    category = models.CharField(max_length=32)
    safety_stock = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.product_name        


class Takeout(models.Model):
    carry_day = models.DateField()
    carry_team = models.CharField(max_length=16)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    receive_company = models.CharField(max_length=32)
    receive_tel = models.CharField(max_length=16)
    receive_user = models.CharField(max_length=16)
    material_name = models.CharField(max_length=64)
    material_info = models.CharField(max_length=64)
    purpose = models.CharField(max_length=64)
    pack_date = models.DateField()
    production_capacity = models.CharField(max_length=32)
    carry_capacity = models.CharField(max_length=32)
    residual_quantity = models.CharField(max_length=32)
    delivery = models.CharField(max_length=16)
    note = models.TextField(null=True, blank=True)
    modify_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.material_name        