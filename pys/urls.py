from django.contrib import admin
from django.urls import path
from pys import views
app_name = 'pys'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("base/", views.base, name= "base"),
    path("child/", views.child, name= "child"),
    path("home/", views.home, name= "home"),
    path("aboutus/", views.aboutus, name= "aboutus"),
    path("gallary/", views.gallary, name= "gallary"),
]