from django.urls import path, include

from . import views
from . import views
urlpatterns = [
        path('profile-edit', views.edit_user_profile, name='edit_user_profile')
]
