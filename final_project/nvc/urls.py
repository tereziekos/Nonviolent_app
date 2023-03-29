from django.urls import path
from .views import homepage, feelings_inventory

urlpatterns = [
    path('', homepage, name='homepage'),
    path('feelings/', feelings_inventory, name='feelings_inventory'),
]