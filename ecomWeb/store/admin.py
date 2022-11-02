from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','age'] 

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'total_price','customer']

@admin.register(Address)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'pincode','h_no','city','customer']

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','brand','category','item_in_carts']