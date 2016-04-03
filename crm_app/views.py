from django.shortcuts import render


# view for the main page
def main_page(request):
    return render(request, 'crm_app/main_page.html')