"""my_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from my_app import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login', 'django.contrib.auth.views.login',name='login'),

    url(r'^$',views.home,name='home'),
    url(r'^guest$',views.guest,name='guest'),
    url(r'^loggedIn$',views.loggedIn,name='loggedIn'),
    url(r'^my_app/(?P<currency_id>\w+)/$', views.detail, name='detail'),
    url(r'^(?P<currency_id>\w+)/rates/$',views.exchange_rates,name='exch_rates'),
]
