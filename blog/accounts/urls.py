from django.urls import path
from .views import RegistrationView


app_name = 'registration'
urlpatterns = [
    path('', RegistrationView.as_view(), name='registration'),
]