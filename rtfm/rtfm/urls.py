"""rtfm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import *
import core.views as v


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/close_session/', v.close_session),
    path('api/open_session/', v.open_session),
    path('api/get_valid_list/', v.get_valid_list),
    path('api/transact', v.transact),
    path('api/close_session/', v.close_session),
    path('api/recent_payments', v.recent_payments),
    path('api/user_info', v.recent_payments),
]
