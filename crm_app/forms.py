from django import forms
from .models import CrmUser, Company


class CrmUserForm(forms.ModelForm):

    class Meta:
        model = CrmUser
        fields = ('username', 'firstname', 'lastname', 'password')


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ('name', 'owner', 'sector', 'number_of_employees')