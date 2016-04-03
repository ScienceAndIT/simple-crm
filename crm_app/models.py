from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class CrmUser(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return 'Profile of user: {}'.format(self.user.username)


class Company(models.Model):
    SECTOR_CHOICES = (
        ('it', 'IT'),
        ('finance', 'Finance'),
        ('education', 'Education')
    )
    NUMBER_OF_EMPLOYEES_CHOICES = (
        ('small', '1-20'),
        ('medium', '21-50'),
        ('large', '51-100'),
        ('xxl', '>100')
    )
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=50)
    sector = models.CharField(max_length=10,
                              choices=SECTOR_CHOICES,
                              default='it')
    number_of_employees = models.CharField(max_length=10,
                                           choices=NUMBER_OF_EMPLOYEES_CHOICES,
                                           default='medium')

    def __str__(self):
        return self.name