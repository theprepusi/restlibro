"""restlibro URL Configuration

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
from api.login.loginapi import LoginAPI, LogoutAPI
from api.libro.libroapi import libroapi
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # LIBROS
    path('api/v1/libro/select/<int:id>/', libroapi.as_view(), name='libroapi'), # URL GET
    path('api/v1/libro/create/', libroapi.as_view(), name='libroapi'), # URL POST
    path('api/v1/libro/update/<int:id>/', libroapi.as_view(), name='libroapi'), # URL PUT
    path('api/v1/libro/delete/<int:id>/', libroapi.as_view(), name='libroapi'), # URL DELETE

    # Login
    path('api/v1/login/', LoginAPI.as_view(), name='LoginAPI'), #URL POST
    path('api/v1/logout/', LogoutAPI.as_view(), name='LogoutAPI'), #URL POST
]

urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
