from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^company/(?P<pk>[0-9]+)/$', views.company_details, name='company_details'),
    url(r'^companies/$', views.companies_view, name='companies'),
    url(r'^add-company/$', views.add_company_view, name='add_company'),
    url(r'^delete-company/(?P<pk>\d+)/$', views.company_delete, name='company_delete'),
    url(r'^users/details/user/(?P<pk>[0-9]+)/$', views.user_details, name='user_details'),
    url(r'^users/$', views.users_view, name='users_view'),
    url(r'^add-user/$', views.add_user_view, name='add_user'),
    url(r'^delete-user/(?P<pk>\d+)/$', views.user_delete, name='user_delete'),
    url(r'^user/(?P<pk>[0-9]+)/edit/$', views.user_edit, name='user_edit'),
    url(r'^password-change/$',
        'django.contrib.auth.views.password_change',
        name='password_change'),
    url(r'^password-change/done/$',
        'django.contrib.auth.views.password_change_done',
        name='password_change_done'),
]