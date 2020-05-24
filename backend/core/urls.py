# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from django.views.generic import TemplateView # <--
from patient import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'patients', views.PatientViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("authentication.urls")),  # add this
    path('', include("app.urls")), # add this
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
