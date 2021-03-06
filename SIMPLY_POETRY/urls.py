"""SIMPLY_POETRY URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

import web.views
from SIMPLY_POETRY import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',web.views.Index.as_view(),name='Index'),
    path('c_yf/<pk>',web.views.CREATE_YFEEL.as_view(),name='C_YF'),
    path('archive/<pk>',web.views.SEEARCHIVE.as_view(),name='Archive')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

