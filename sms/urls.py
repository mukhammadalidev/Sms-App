from django.urls import path
from .views import SendPhoneNumber
urlpatterns = [
        path('send_phone_number/',SendPhoneNumber.as_view())
]