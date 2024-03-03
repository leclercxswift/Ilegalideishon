from django.urls import path
from .views import register, user_login, index, download_pdf, inicio, horario_view

urlpatterns = [
    path('', inicio, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('index/', index, name='index'),
    path('download-pdf/', download_pdf, name='download_pdf'),
    path('horario/', horario_view, name='horario_view'),
]
