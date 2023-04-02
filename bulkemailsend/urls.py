from django.urls import path
from .views import homeView, emailSend

urlpatterns = [
    path('', homeView, name='home'),
    path('email', emailSend, name='email')
]
