import uuid

from django.db import models
from decimal import Decimal
from prints.models import Print
from django.db.models import Sum
from django.conf import settings
from django_countries.fields import CountryField

from profiles.models import RegisteredUserProfile


class Order(models.Model):
    stripe_pid = models.CharField(max_length=254,
                                  null=False,
                                  blank=False,
                                  default='')
    customer = models.ForeignKey(RegisteredUserProfile,
                                 null=True,
                                 on_delete=models.CASCADE)
    order_number = models.CharField(max_length=32,
                                    null=False,
                                    editable=False)
    date = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=50,
                                 null=False,
                                 blank=False)
    email = models.EmailField(max_length=254,
                              null=False,
                              blank=False)
    phone_number = models.CharField(max_length=20,
                                    null=False,
                                    blank=False)
    street_address_1 = models.CharField(max_length=80,
                                        null=False,
                                        blank=False)
    street_address_2 = models.CharField(max_length=80,
                                        null=False,
                                        blank=False)
    town = models.CharField(max_length=50,
                            null=True,
                            blank=True)
    country = CountryField(blank_label='Country',
                           null=False,
                           blank=False)
    postcode = models.CharField(max_length=10,
                                null=False,
                                blank=False)
    delivery_cost = models.DecimalField(max_digits=8,
                                        decimal_places=2,
                                        null=False,
                                        default=0)
    order_total = models.DecimalField(max_digits=8,
                                      decimal_places=2,
                                      null=False,
                                      default=0)
    grand_total = models.DecimalField(max_digits=8,
                                      decimal_places=2,
                                      null=False,
                                      default=0)

    def _generate_order_number(self):
        """ Generate a random 32 digit order number """

        return uuid.uuid4().hex.upper()

    def update_total(self):
        """ Update grand total each time an item is added"""
        """ accounting for delivery costs """

        self.order_total = self.lineitems.aggregate(
                                Sum(
                                    'lineitem_total')
                                    )['lineitem_total__sum'] or 0
        self.delivery_cost = self.order_total * Decimal(
                                  settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """ Override original save method to set order number """
        """ (if hasn't been done already) """

        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order,
                              null=False,
                              blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    print_details = models.ForeignKey(Print,
                                      null=False,
                                      blank=False,
                                      on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False,
                                   blank=False,
                                   default=0)
    lineitem_total = models.DecimalField(max_digits=10,
                                         decimal_places=2,
                                         null=False,
                                         blank=False,
                                         editable=False)

    def save(self, *args, **kwargs):
        """ Override original save method to set order number """
        """ (if hasn't been done already) """

        self.lineitem_total = self.print_details.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.lineitem_total)
