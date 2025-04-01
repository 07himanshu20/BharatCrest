#use portfolio for routing in the first route
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('portfolio.urls')),
]
