from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name="index"),
#path('newsletter/', views.email_send, name='index'),
    path('register/', views.register, name='register'),
    path('register_save', views.register_save, name='register_save'),
    path('send_email', views.send_email, name='send_email'),
]