# dashboard urls links
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.dashboard_home, name='home_dashboard'),  # dashboard homepage
    path('manage-jobs/', views.manage_jobs, name='manage-jobs'),
    path('manage-resume/', views.manage_resume, name='manage-resume'),
    path('reviews/', views.manage_resume, name='reviews'),
]
