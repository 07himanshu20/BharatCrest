#use portfolio for routing in the first route
from django.contrib import admin
from django.urls import path,include

def home_redirect(request):
    return redirect('portfolio/')  # Redirects to portfolio app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('portfolio/',include('portfolio.urls')),
]
