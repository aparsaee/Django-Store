# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse


class Brand(models.Model):
    name = models.CharField(
        max_length=200, help_text="Enter a mobile manufacturer (e.g. Samsung, HTC).")
    country = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, primary_key=True)

    def get_absolute_url(self):
        return reverse('brand-detail', args=[str(self.slug)])

    def __str__(self):
        return self.name


class Mobile(models.Model):
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, primary_key=True)
    review = models.TextField(
        max_length=1000, help_text="Enter a review for the mobile")
    operating_system = models.CharField(max_length=200, null=True)
    screen_technology = models.CharField(max_length=200, null=True)
    screen_size = models.FloatField()
    price = models.CharField(max_length=200, null=True)
    repository = models.IntegerField(null=True, blank=True)
    MOBILE_STATUS = (
        ('a', 'Available'),
        ('u', 'Unavailable'),
        ('o', 'Outdated'),
    )

    status = models.CharField(max_length=1, choices=MOBILE_STATUS,
                              blank=True, default='a', help_text='Mobile availability')

    def get_absolute_url(self):
        return reverse('mobile-detail', args=[str(self.slug)])

    def __str__(self):
        return self.name


class Sold(models.Model):
    customer = models.ForeignKey('auth.User')
    brand = models.CharField(max_length=200, null=True)
    product = models.CharField(max_length=200, null=True)
    amount = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    address = models.CharField(max_length=2000, null=True)
    phone = models.CharField(max_length=11, null=True)
    zip_code = models.CharField(max_length=10, null=True)
