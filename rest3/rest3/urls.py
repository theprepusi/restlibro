"""rest3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from api.login.LoginAPI import LoginAPI, LogoutAPI
from api.cuenta.CuentaAPI import CuentaAPI
from api.usuario.UsuarioAPI import UsuarioAPI
from api.fabricante.FabricanteAPI import FabricanteAPI
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # FABRICANTES
    path('api/v1/fabricante/select/', FabricanteAPI.as_view(), name='FabricanteAPI'), # URL GET
    path('api/v1/fabricante/create/', FabricanteAPI.as_view(), name='FabricanteAPI'), # URL POST
    path('api/v1/fabricante/update/<int:id>/', FabricanteAPI.as_view(), name='FabricanteAPI'), # URL PUT
    path('api/v1/fabricante/delete/<int:id>/', FabricanteAPI.as_view(), name='FabricanteAPI'), # URL DELETE

    # USUARIOS
    path('api/v1/usuario/select/', UsuarioAPI.as_view(), name='UsuarioAPI'), # URL GET

    # CUENTA
    path('api/v1/cuenta/select/<int:id>/', CuentaAPI.as_view(), name='CuentaAPI'), # URL GET

    # Login
    path('api/v1/login/', LoginAPI.as_view(), name='LoginAPI'), #URL POST
    path('api/v1/logout/', LogoutAPI.as_view(), name='LogoutAPI'), #URL POST
]

urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
