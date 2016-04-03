from django.shortcuts import render


# view all companies
def companies_view(request):
    return render(request, 'crm_app/companies.html')


# view all users
def users_view(request):
    return render(request, 'crm_app/users.html')


# add another company
def add_company_view(request):
    return render(request, 'crm_app/add_company.html')


# add another user
def add_user_view(request):
    return render(request, 'crm_app/add_user.html')