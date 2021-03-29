from .views import SaleView
from django.urls import path

urlpatterns = [
    path('new-sale/', SaleView.as_view()),
]
