from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('transactions/', include('apps.transactions.urls')),
    path('', views.home_page, name='home'),
]