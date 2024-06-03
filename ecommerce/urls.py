from django.contrib import admin
from django.urls import path

from .import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Master, name='master'),
    path('index/', views.Index, name='index'),
]
