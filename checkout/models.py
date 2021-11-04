from django.db import models
from decimal import *
from datetime import datetime  

# Create your models here.

import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from products.models import Product
from profiles.models import UserProfile


class Order(models.Model):
    order_number = models.CharField(max_length=254, null=False, editable=False)  #32
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=254, null=False, blank=False)  #50
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=254, null=False, blank=False)  # 20

    country = CountryField(blank_label='Country *', null=False, blank=False)
    
    postcode = models.CharField(max_length=254, null=True, blank=True)  # 20
    town_or_city = models.CharField(max_length=254, null=False, blank=False)  # 40
    street_address1 = models.CharField(max_length=254, null=False, blank=False)  # 80
    street_address2 = models.CharField(max_length=254, null=True, blank=True)  # 80
    county = models.CharField(max_length=254, null=True, blank=True)  # 80

    #date = models.DateTimeField(auto_now_add=True)
    date = models.SlugField(default=datetime.now, blank=True)

    #delivery_cost = models.SlugField(null=False, default=0)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=4, null=False, default=0)

    #order_total = models.SlugField(null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=4, null=False, default=0)

    #grand_total = models.SlugField(null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=4, null=False, default=0)

    #original_bag = models.SlugField(null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')

    #stripe_pid = models.SlugField(null=False, default=0)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = settings.STANDARD_DELIVERY_PERCENTAGE
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost

        getcontext().prec = 4

        self.grand_total = Decimal(self.grand_total)
        print('Decimal(self.grand_total)')
        print(self.grand_total)
        print('-----------------------')
        
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    size = models.CharField(max_length=254, null=True, blank=True)  # 8
    quantity = models.IntegerField(null=False, blank=False, default=0)
    # lineitem_total = models.SlugField(null=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=4, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total, depending on item size
        """

        constant = 1
        if not self.size:
            constant = self.product.price
        if self.size  == "small":
            constant = self.product.price
        if self.size == "medium":
            constant = self.product.price + 12
        if self.size == "large":
            constant = self.product.price + 20
        
        self.lineitem_total = constant * self.quantity

        getcontext().prec = 4
        self.lineitem_total = Decimal(self.lineitem_total)
        print('self.lineitem_total')
        print(self.lineitem_total)
        print('-----------------------')

        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'