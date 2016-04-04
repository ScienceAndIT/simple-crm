from django import forms
from django.contrib.auth.models import User
from .models import Company


class CrmUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password')


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ('name', 'owner', 'sector', 'number_of_employees', 'added_by')