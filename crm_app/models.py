from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class CrmUser(models.Model):
    user = models.OneToOneField(User)
    # new fields can be added here to extend this model
    added_by = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.user.username


class Company(models.Model):
    SECTOR_CHOICES = (
        ('IT', 'IT'),
        ('Finance', 'Finance'),
        ('Education', 'Education')
    )
    NUMBER_OF_EMPLOYEES_CHOICES = (
        ('1-20', '1-20'),
        ('21-50', '21-50'),
        ('51-100', '51-100'),
        ('>100', '>100')
    )
    name = models.CharField(max_length=100, blank=False)
    owner = models.CharField(max_length=50, blank=False)
    sector = models.CharField(max_length=10,
                              choices=SECTOR_CHOICES,
                              default='it')
    number_of_employees = models.CharField(max_length=10,
                                           choices=NUMBER_OF_EMPLOYEES_CHOICES,
                                           default='medium')
    added_by = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.name