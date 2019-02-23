from django.urls import path
from . import views

app_name = 'jobs'
urlpatterns = [
    path('', views.index, name='list of jobs'),
    path('<int:job_id>/', views.job_detail, name='job detail'),
    path('<int:job_id>/edit', views.job_edit, name='edit job'),
    path('<int:job_id>/update', views.job_update, name='update job'),
    path('designers/', views.designers_list, name='list of designers'),
    path('designers/<int:designer_id>/', views.designer_detail, name='designer detail'),
]

