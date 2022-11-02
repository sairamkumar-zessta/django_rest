from django.db import models

class Customer(models.Model):
    name = models.CharField( max_length=100 ) 
    age = models.IntegerField() 
#one-to-one relation
class Cart (models.Model):
    total_price = models.IntegerField()
    customer = models.OneToOneField(Customer,on_delete=models.CASCADE)
#many-to-one-relation
class Address(models.Model):
    pincode = models.IntegerField() 
    h_no = models.CharField(max_length=100) 
    city = models.CharField(max_length=200) 
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)

#many-to-many 
class Products(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    brand = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    cart = models.ManyToManyField(Cart)

    def item_in_carts(self):
        return ",".join([str(c.customer.name) for c in self.cart.all()])
