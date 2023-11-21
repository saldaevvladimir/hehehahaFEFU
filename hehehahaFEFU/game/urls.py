from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page, name='main'),
    path('login', user_log, name='login'),
    path('register', user_reg, name='register')
]
