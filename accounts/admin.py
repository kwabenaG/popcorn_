from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.conf import settings


# local apps
from .models import UserProfile, CustomUser  # local models
from .forms import SignUpForm

# CustomUser = get_user_model()  # signifies the user the model


class CustomUserAdmin(admin.ModelAdmin):
    list_filter = ['username', 'email']
    list_display = ['username', 'first_name', 'last_name', 'email', 'is_superuser']
    model = settings.AUTH_USER_MODEL
    form = SignUpForm
    fields = ('username', 'first_name', 'last_name',
              'email', 'password1', 'password2', 'is_superuser', 'is_staff', 'is_active', )


class CustomProfileAdmin(admin.ModelAdmin):
    list_filter = ['dob']
    list_display = ['userCreated', 'dob', 'student_number', 'school', 'program', 'phone_number']
    model = UserProfile
    fields = (
        'userCreated', 'dob', 'gender', 'country', 'phone_number', 'student_number', 'school', 'program', 'start_program',
        'complete_program', 'qualification', 'company_name', 'company_location', 'job_position',
        'job_position_period_from', 'job_position_period_to', 'resume', 'profile_img', 'region'
    )


# register models
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile, CustomProfileAdmin)

