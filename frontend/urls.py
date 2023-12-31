from django.urls import path

from .views import *

app_name = "frontend"
urlpatterns = [
    path('', home_view, name='home'),
    path('registration/', registration_view, name='registration'),
    path('verify_code/<str:code>/', verify_code_view, name='verify_code'),
    path('logout/', logout_view, name='logout'),
]
