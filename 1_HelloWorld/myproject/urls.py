from django.contrib import admin
from django.urls import path
import HelloWorld.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HelloWorld.views.home, name= "home"),
]
