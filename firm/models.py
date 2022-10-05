from django.db import models

from django.contrib.auth.models import User

from users.models import Auth_User


# Create your models here.
class Firm(models.Model):
    f_name=models.CharField(max_length=20)
    phone=models.CharField(max_length=12)
    address=models.TextField(blank=True)

    def __str__(self):
        return self.name

    # class Meta:
    #     verbose_name_plural = "Firms"


class Category(models.Model):
    c_name=models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Brand(models.Model):
    b_name=models.CharField(max_length=20)
    

    def __str__(self):
        return self.name


class Product(models.Model):
    
    p_name=models.CharField(max_length=20)
    category=models.OneToOneField(Category, on_delete=models.CASCADE, blank=True, null=True) 
    brand=models.OneToOneField(Brand, on_delete=models.CASCADE, blank=True, null=True) 
    stock=models.SmallIntegerField()

    def __str__(self):
        return f"{self.name} - {self.category} - {self.brand}"




class Stock(models.Model):
    user=models.OneToOneField(Auth_User, on_delete=models.CASCADE)  #related_name='stuser'
    firm=models.OneToOneField(Firm, on_delete=models.CASCADE)       # related_name='stfirm'
    transaction=models.CharField(max_length=20)
    product=models.OneToOneField(Product, on_delete=models.PROTECT, related_name='stproduct')
    quantity=models.SmallIntegerField()
    price=models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    price_total=models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.firm} - {self.product} - {self.quantity}"
    

