from django.contrib import admin
from django.urls import path
from transporte.views.usuario.usuario_login import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login ,name='login'),
]
