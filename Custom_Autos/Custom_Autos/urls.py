from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name="login"),
    path('', TemplateView.as_view(template_name="home.html"), name="home"),
    path('vehicle/', include('vehicle.urls')),
]


