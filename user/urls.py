from .views import LoginPage,LoginView,RedirectView
from django.urls import path

urlpatterns = [
    path('', LoginPage.as_view()),
    path('login/', LoginView.as_view()),
    path('menu-redirect/',RedirectView.as_view()),
]
