from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('jobs/', include('jobs.urls')),
    path('admin/', admin.site.urls),
]
