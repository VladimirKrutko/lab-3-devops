from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', include('rest_store_api.urls')),
    path('admin/', admin.site.urls),
]
