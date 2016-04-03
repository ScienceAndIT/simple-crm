from django.conf.urls import include, url
from . import views

urlpatterns = [
    #url(r'^zaloguj/$', views.user_login, name='login'),
    url(r'login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'companies/$', views.companies_view, name='companies'),
    url(r'add-company/$', views.companies_view, name='companies'),
    url(r'^password-change/$',
        'django.contrib.auth.views.password_change',
        name='password_change'),
    url(r'^done-password-change/$',
        'django.contrib.auth.views.password_change_done',
        name='password_change_done'),
    url(r'^$', views.companies_view, name='companies_view'),
    ]