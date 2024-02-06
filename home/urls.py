from django.urls import path
from .views import main_page

app_name = 'home'

urlpatterns = [
    path('', main_page, name='main_page'),
]
