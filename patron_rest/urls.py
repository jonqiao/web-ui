"""patron_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

import patron_app.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tenants/$', patron_app.views.tenants),
    url(r'^models/(.+)/$', patron_app.views.models),
    url(r'^tenants/(\w+)/$', patron_app.views.metadata),
    url(r'^tenants/(\w+)/policies/(.+)/$', patron_app.views.policy),
    url(r'^tenants/(\w+)/users/$', patron_app.views.users),
    url(r'^tenants/(\w+)/users/(.+)/commands/$', patron_app.views.commands),
    url(r'^tenants/(\w+)/users/(.+)/commands/(.*)$', patron_app.views.command),
    url(r'^reset/$', patron_app.views.reset),
    url(r'^(.*).html$', patron_app.views.redirect_handler),
    url(r'^$', patron_app.views.mainpage_handler)
]
