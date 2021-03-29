from .views import MenuView, InsertItem
from django.urls import path

urlpatterns = [
    path('menu/', MenuView.as_view()),
    path('item/', InsertItem.as_view()),
]
