import random
from django.contrib.auth import get_user_model  # uses the base db when use get_user_model
from django.contrib.auth.forms import forms

from .models import UserProfile, CustomUser

# third party
# from allauth.account.forms import LoginForm
from phonenumber_field.formfields import PhoneNumberField


# overrides django allauth
class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(max_length=200, widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=200, widget=forms.PasswordInput())

    # called this to override init constructor because i wanted to style the password field and other fields
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'utf-with-border', 'placeholder': 'Username'})
        self.fields['email'].widget = forms.EmailInput(attrs={'class': 'utf-with-border', 'placeholder': 'Email'})

        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'utf-with-border', 'name': 'password1', 'placeholder': 'Password'})

        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'utf-with-border', 'name': 'password2', 'placeholder': 'Repeat Password'})

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def signup(self, request, user, *args, **kwargs):
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']
        user.save()
        return user


# USER DATA ie for print etc..
class RealUserData(forms.ModelForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'utf-submit-field', 'readonly': True}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'utf-submit-field', 'readonly': True}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'utf-submit-field', 'readonly': True}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'utf-submit-field', 'readonly': True}))

    class Meta:
        model = get_user_model()
        fields = [
            'email', 'first_name', 'last_name', 'username'
        ]


# USER PROFILE DATA ie for print etc..
class RealUserProfileData(forms.ModelForm):

    gender = forms.CharField(widget=forms.Select(attrs={'class': 'utf-with-border','readonly': True}))
    dob = forms.DateField(widget=forms.DateInput(format="%d/%m/%Y",
                                                 attrs={'class': 'utf-with-border', 'type': 'date','readonly': True}), )
    country = forms.CharField(widget=forms.TextInput(attrs={'class': 'utf-with-border','readonly': True}))
    phone_number = PhoneNumberField(widget=forms.TextInput(attrs={'class': 'utf-with-border',
                                                                  'readonly': True}))
    region = forms.CharField(widget=forms.TextInput(attrs={'class': 'utf-with-border', 'readonly': True}))
    student_number = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'utf-with-border', 'readonly': True}))
    school = forms.CharField(required=False, error_messages={'required': 'The school field is required'},
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control',
                                        'readonly': True}))
    start_program = forms.DateField(widget=forms.DateInput(format="%d/%m/%Y",
                                                           attrs={'class': 'utf-with-border', 'type': 'date','readonly': True}), )
    complete_program = forms.DateField(widget=forms.DateInput(format="%d/%m/%Y",
                                                              attrs={'class': 'utf-with-border',
                                                                     'type': 'date', 'readonly': True}), )
    program = forms.CharField(widget=forms.TextInput(attrs={'class': 'utf-with-border','readonly': True}))
    qualification = forms.CharField(widget=forms.Select(attrs={'class': 'utf-with-border','readonly': True}))
    company_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'utf-with-border', 'readonly': True}))
    company_location = forms.CharField(widget=forms.TextInput(attrs={'class': 'utf-with-border', 'readonly': True}))
    job_position = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'utf-with-border', 'readonly': True}))
    job_position_period_from = forms.DateField(
        widget=forms.DateInput(format="%d/%m/%Y",
                               attrs={
                                   'class': 'utf-with-border', 'type': 'date','readonly': True},) )
    job_position_period_to = forms.DateField(
        widget=forms.DateInput(format="%d/%m/%Y",
                               attrs={
                                   'class': 'utf-with-border', 'type': 'date','readonly': True}), )
    resume = forms.FileField(widget=forms.FileInput(
        attrs={'class': 'utf-with-border', 'type': 'file'}))
    profile_img = forms.FileField(widget=forms.FileInput(
        attrs={'type': 'file', 'class': 'file-upload', 'required': False}))

    # role = forms.BooleanField(widget=forms.RadioSelect(attrs={'class': 'radio'}, choices=ROLE))

    class Meta:
        model = UserProfile
        fields = [
            'dob', 'gender', 'country', 'phone_number', 'student_number', 'school', 'program', 'start_program',
            'complete_program', 'qualification', 'company_name', 'company_location', 'job_position',
            'job_position_period_from', 'job_position_period_to', 'resume', 'profile_img', 'region'
        ]

# ============================================================================================================#

# updates the user and profile info


class UpdateUserForm(forms.ModelForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'utf-submit-field'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'utf-submit-field'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'utf-submit-field'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'utf-submit-field'}))

    class Meta:
        model = get_user_model()
        fields = [
            'email', 'first_name', 'last_name', 'username'
        ]


class UpdateProfileForm(forms.ModelForm):
    ROLE = (
        ('student', 'Student'),
        ('staff', 'Staff')
    )
    GENDER = (
        (None, 'Select Gender'),
        ('Male', 'Male'),
        ('Female', 'Female'))

    DEGREE = (
        (None, 'Select your qualifications'),
        ('Undergraduate', 'Undergraduate'),
        ('Bachelor', 'Bachelor (BSc)'),
        ('Master', 'Master (Msc, MPHIL)'),
        ('PhD', 'PhD')
    )
    gender = forms.CharField(widget=forms.Select(attrs={'class': 'utf-with-border'}, choices=GENDER))
    dob = forms.DateField(widget=forms.DateInput(format="%d/%m/%Y",
                                                 attrs={'class': 'utf-with-border', 'type': 'date'}),)
    country = forms.CharField(widget=forms.TextInput(attrs={'class': 'utf-with-border', 'placeholder': 'Eg. Ghana'}))
    phone_number = PhoneNumberField(widget=forms.TextInput(attrs={'class': 'utf-with-border',
                                                                  'placeholder': 'eg. +233 268971089'}))
    region = forms.CharField(widget=forms.TextInput(attrs={'class': 'utf-with-border', 'placeholder': 'Eg. Accra', }))
    student_number = forms.IntegerField(widget=forms.TextInput(
        attrs={'class': 'utf-with-border', 'readonly': True,
               'value': random.randint(1000, 1000091)}))
    school = forms.CharField(required=False, error_messages={'required': 'The school field is required'},
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control',
                                        'placeholder': 'Eg. Kwame Nkrumah University Of Science and Techonlogy (KNUST)'}))
    start_program = forms.DateField(widget=forms.DateInput(format="%d/%m/%Y",
                                                           attrs={'class': 'utf-with-border', 'type': 'date'}),)
    complete_program = forms.DateField(widget=forms.DateInput(format="%d/%m/%Y",
                                                              attrs={'class': 'utf-with-border',
                                                                     'type': 'date', 'required': False}),)
    program = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'utf-with-border', 'placeholder': 'Eg. Computer Science'}))
    qualification = forms.CharField(widget=forms.Select(attrs={'class': 'utf-with-border'}, choices=DEGREE))
    company_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'utf-with-border', 'placeholder': 'Eg. MTN'}))
    company_location = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'utf-with-border', 'placeholder': 'Eg. Accra, Kumasi, Cape Coast etc..'}))
    job_position = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'utf-with-border', 'placeholder': 'Eg. Intern Supervisor'}))
    job_position_period_from = forms.DateField(
        widget=forms.DateInput(format="%d/%m/%Y",
                               attrs={
                                   'class': 'utf-with-border', 'type': 'date'}),)
    job_position_period_to = forms.DateField(
        widget=forms.DateInput(format="%d/%m/%Y",
                               attrs={
                                   'class': 'utf-with-border', 'type': 'date'}),)
    resume = forms.FileField(widget=forms.FileInput(
        attrs={'class': 'utf-with-border', 'type': 'file'}))
    profile_img = forms.FileField(widget=forms.FileInput(
        attrs={'type': 'file', 'class': 'file-upload', 'required':  False}))
    # role = forms.BooleanField(widget=forms.RadioSelect(attrs={'class': 'radio'}, choices=ROLE))

    class Meta:
        model = UserProfile
        fields = [
            'dob', 'gender', 'country', 'phone_number', 'student_number', 'school', 'program', 'start_program',
            'complete_program', 'qualification', 'company_name', 'company_location', 'job_position',
            'job_position_period_from', 'job_position_period_to', 'resume', 'profile_img', 'region'
        ]


