from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from watson import search as watson


class CrmUser(models.Model):
    user = models.OneToOneField(User)
    # new fields can be added here to extend this model

    def __str__(self):
        return self.user.username

    def __unicode__(self):
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
    name = models.CharField(max_length=100, blank=False, unique=True)
    owner = models.CharField(max_length=50, blank=False)
    sector = models.CharField(max_length=10,
                              choices=SECTOR_CHOICES,
                              default='IT')
    number_of_employees = models.CharField(max_length=10,
                                           choices=NUMBER_OF_EMPLOYEES_CHOICES,
                                           default='21-50')
    added_by = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('company_details', args=[self.pk])

# preparing watson to search in Company's objects
#watson.register(Company)