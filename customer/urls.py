from .views import CustomerView
from django.urls import path

urlpatterns = [
    path('customer/', CustomerView.as_view()),
]
