from django.urls import path
from . import views

urlpatterns = [
    path('get_first_message', views.get_first_message),
path('get_chat_response', views.chat_response), 
]