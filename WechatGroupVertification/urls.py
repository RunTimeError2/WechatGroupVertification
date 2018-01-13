"""
Definition of urls for WechatGroupVertification.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

#import app.forms
#import app.views
import WeChat.views

# Uncomment the next lines to enable the admin: 
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    
    #url(r'^$', app.views.home, name='home'),
    #url(r'^contact$', app.views.contact, name='contact'),
    #url(r'^about', app.views.about, name='about'),
    #url(r'^login/$',
    #    django.contrib.auth.views.login,
    #    {
    #        'template_name': 'app/login.html',
    #        'authentication_form': app.forms.BootstrapAuthenticationForm,
    #        'extra_context':
    #        {
    #            'title': 'Log in',
    #            'year': datetime.now().year,
    #        }
    #    },
    #    name='login'),
    #url(r'^logout$',
    #    django.contrib.auth.views.logout,
    #    {
    #        'next_page': '/',
    #    },
    #    name='logout'),
    
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', WeChat.views.WxMain, name = 'WxMain'),
]
