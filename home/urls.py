from django.urls import path
# from .views import main_page
from .views import MainPageView

app_name = 'home'

urlpatterns = [
    # path('', main_page, name='main_page'),
    path('', MainPageView.as_view(), name='main_page'),
]
