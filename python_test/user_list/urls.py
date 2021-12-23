from django.conf import settings
from django.urls import path

from user_list import views

urlpatterns = [
    path("", views.Customer.as_view(), name="customer"),
]
