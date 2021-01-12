from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import BlogViewSet

routers = routers.DefaultRouter()
routers.register('blog', BlogViewSet)

urlpatterns = [
    path('', include(routers.urls)),
]