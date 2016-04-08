from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from . forms import CompanyForm, CrmUserForm
from .models import Company


# view all companies
@login_required
def companies_view(request):
    object_list = Company.objects.order_by('name')
    paginator = Paginator(object_list, 5)  # 5 companies on each page
    page = request.GET.get('page')
    try:
        companies = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        companies = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        companies = paginator.page(paginator.num_pages)
    return render(request, 'crm_app/companies.html',
                  {'page': page,
                   'companies': companies})


# view all users
@login_required
def users_view(request):
    object_list = User.objects.order_by('username')
    paginator = Paginator(object_list, 3)  # 3 users on each page
    page = request.GET.get('page')
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        users = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        users = paginator.page(paginator.num_pages)
    return render(request, 'crm_app/users.html',
                  {'page': page,
                   'users': users})


# details of the user
def user_details(request, pk):
    my_user = get_object_or_404(User, pk=pk)
    return render(request, 'crm_app/user_details.html', {'my_user': my_user})


# details of the company
def company_details(request, pk):
    my_company = get_object_or_404(Company, pk=pk)
    return render(request, 'crm_app/company_details.html', {'my_company': my_company})


# add another company
@login_required
def add_company_view(request):
    if request.method == 'POST':
        company_form = CompanyForm(request.POST)
        if company_form.is_valid():
            new_company = company_form.save(commit=True)
            return render(request,
                          'crm_app/add_company_done.html',
                          {'new_company': new_company})
    else:
        company_form = CompanyForm()
    return render(request, 'crm_app/add_company.html',
                  {'company_form': company_form})


# add another user
@login_required
def add_user_view(request):
    if request.method == 'POST':
        user_form = CrmUserForm(request.POST)
        user_adder = request.user.username
        if user_form.is_valid():
            # new user (not saved yet)
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password'])
            # now, we can save new user
            new_user.save()
            return render(request,
                          'crm_app/add_user_done.html', {'new_user': new_user})
    else:
        user_form = CrmUserForm()
        user_adder = request.user.username
    return render(request, 'crm_app/add_user.html',
                  {'user_form': user_form,
                   'user_adder': user_adder})


# delete company
@login_required
def company_delete(request, pk):
    company_to_delete = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        company_to_delete.delete()
        return redirect('companies')
    return render(request,
                  'crm_app/company_confirm_delete.html',
                  {'object': company_to_delete})


# delete user
@login_required
def user_delete(request, pk):
    user_to_delete = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user_to_delete.delete()
        return redirect('users_view')
    return render(request,
                  'crm_app/user_confirm_delete.html',
                  {'object': user_to_delete})


# edit details of the user
@login_required
def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = CrmUserForm(request.POST, instance=user)
        if form.is_valid():
            #user = form.save(commit=False)
            #user.author = request.user
            form.save()
            return redirect('users_view')
        else:
            return redirect('companies')
    else:
        form = CrmUserForm(instance=user)
    return render(request,
                  'crm_app/user_edit.html',
                  {'form': form})