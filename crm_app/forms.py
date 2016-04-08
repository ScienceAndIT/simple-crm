from django import forms
from django.contrib.auth.models import User
from .models import Company, CrmUser


class CrmUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password')

"""
# for later
class CrmUserForm2(forms.ModelForm):

    class Meta:
        model = CrmUser
        exclude = ['user']
        widgets = {'added_by': forms.HiddenInput()}
"""


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ('name', 'owner', 'sector', 'number_of_employees', 'added_by')