from django.urls import path
from . import views

app_name = 'jobs'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:job_id>/', views.job_detail, name='job detail'),
    path('title/', views.add_title, name='add title'),
    path('designers/', views.designers_list, name='list of designers'),
    path('designers/<int:designer_id>/', views.designer_detail, name='designer detail'),
]

