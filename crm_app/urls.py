from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^zaloguj/$', views.user_login, name='login'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^companies/$', views.companies_view, name='companies'),
    url(r'^add-company/$', views.add_company_view, name='add_company'),
    url(r'^users/$', views.users_view, name='users_view'),
    url(r'^add-user/$', views.add_user_view, name='add_user'),
    url(r'^password-change/$',
        'django.contrib.auth.views.password_change',
        name='password_change'),
    url(r'^done-password-change/$',
        'django.contrib.auth.views.password_change_done',
        name='done_password_change'),
    ]