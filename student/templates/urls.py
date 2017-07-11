from django.conf.urls import url
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views as student_views
from django.contrib.auth.views import (
     password_reset, password_reset_done, password_reset_confirm,
    password_reset_complete
)
urlpatterns =[

	url(r'^$', student_views.home, name ='home'),
	url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
	url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
	url(r'^signup/$', student_views.signup, name='signup'),
	url(r'^change=password/$', student_views.change_password, name='change_password'),
	url(r'^reset=password/$', password_reset, name='reset_password'),

	 url(r'^reset-password/done/$', password_reset_done, {'template_name': 'reset_password_done.html'}, name='password_reset_done'),

    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'template_name': 'reset_password_confirm.html', 'post_reset_redirect': 'student:password_reset_complete'}, name='password_reset_confirm'),

    url(r'^reset-password/complete/$', password_reset_complete,{'template_name': 'reset_password_complete.html'}, name='password_reset_complete')
]