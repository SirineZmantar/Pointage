from django.conf.urls import url
from . import views

app_name = 'auth'

urlpatterns = [
     url(r'signin/', views.login_user, name='login_user'),
     
]