
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
