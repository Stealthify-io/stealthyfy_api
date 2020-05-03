from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from core.views import UserViewSet


router = routers.DefaultRouter()
router.register(r'user/signup', UserViewSet)

from .views import *

urlpatterns = [
    path('distance', distance),
    path('places', places),
    url(r'^', include(router.urls)),
    path('user/login', login),
]
