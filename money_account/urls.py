from django.urls import path
from .views import money_login, log_out
urlpatterns = [
    path('login/', money_login, name='money_login'),
    path('log-out', log_out, name='log_out'),
]
