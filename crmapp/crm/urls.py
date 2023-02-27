from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers
from .views import CustomerViewSet, LocationViewSet, CustomerMainInfoViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register('customers', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
