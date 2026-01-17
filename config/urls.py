from django.contrib import admin
from django.urls import path, include
from projects.views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path('projects/', include('projects.urls'))
]
