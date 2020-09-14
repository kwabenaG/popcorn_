#
# from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import forms
#
# from popcorn.accounts.models import UserProfile, CustomUser
#
#
# # third party
# # from allauth.account.forms import LoginForm
# from phonenumber_field.formfields import PhoneNumberField
#
#
# # overrides django allauth
# class SignUpForm(forms.ModelForm):
#     password1 = forms.CharField(max_length=200, widget=forms.PasswordInput())
#     password2 = forms.CharField(max_length=200, widget=forms.PasswordInput())
#
#     # called this to override init constructor because i wanted to style the password field
#     def __init__(self, *args, **kwargs):
#         super(SignUpForm, self).__init__(*args, **kwargs)
#         self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
#         self.fields['emails'].widget = forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
#
#         self.fields['password1'].widget = forms.PasswordInput(
#             attrs={'class': 'form-control', 'name': 'password1'})
#
#         self.fields['password2'].widget = forms.PasswordInput(
#             attrs={'class': 'form-control', 'name': 'password2'})
#
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'emails', 'password1', 'password2']
#
#     def signup(self, request, user, **kwargs):
#         user.password1 = self.cleaned_data['password1']
#         user.password2 = self.cleaned_data['password2']
#         user.save()
#         return user
#
#
# # updates the user and profile
# class UpdateUserForm(forms.ModelForm):
#     emails = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
#     first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#
#     class Meta:
#         model = get_user_model()
#         fields = [
#             'emails', 'first_name', 'last_name'
#         ]
#
#
# class UpdateProfileForm(forms.ModelForm):
#     ROLE = (
#         ('student', 'Student'),
#         ('staff', 'Staff')
#     )
#     GENDER = (
#         (None, 'Select Gender'),
#         ('Male', 'Male'),
#         ('Female', 'Female'))
#
#     DEGREE = (
#         (None, 'Select your qualifications'),
#         ('Undergraduate', 'Undergraduate'),
#         ('Bachelor', 'Bachelor (BSc)'),
#         ('Master', 'Master (Msc, MPHIL)'),
#         ('PhD', 'PhD')
#     )
#     gender = forms.CharField(widget=forms.Select(attrs={'class': 'form-control'}, choices=GENDER))
#     dob = forms.DateField(widget=forms.DateInput(format="%d/%m/%Y",
#                                                  attrs={'class': 'form-control datetimepicker'}),
#                           input_formats=("%d/%m/%Y",)
#                           )
#     country = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     phone_number = PhoneNumberField()
#     region = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     student_number = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     school = forms.CharField(required=False, error_messages={'required': 'The school field is required'},
#                              widget=forms.TextInput(attrs={'class': 'form-control'}))
#     start_program = forms.DateField(widget=forms.DateInput(format="%d/%m/%Y",
#                                                            attrs={'class': 'form-control datetimepicker'}),
#                                     input_formats=("%d/%m/%Y",)
#                                     )
#     complete_program = forms.DateField(widget=forms.DateInput(format="%d/%m/%Y",
#                                                               attrs={'class': 'form-control datetimepicker'}),
#                                        input_formats=("%d/%m/%Y",)
#                                        )
#     program = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     qualification = forms.CharField(widget=forms.Select(attrs={'class': 'form-control'}, choices=DEGREE))
#     company_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     company_location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     job_position = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     job_position_period_from = forms.DateField(
#         widget=forms.DateInput(format="%d/%m/%Y",
#                                attrs={
#                                    'class': 'form-control datetimepicker'}),
#         input_formats=("%d/%m/%Y",)
#     )
#     job_position_period_to = forms.DateField(
#         widget=forms.DateInput(format="%d/%m/%Y",
#                                attrs={
#                                    'class': 'form-control datetimepicker'}),
#         input_formats=("%d/%m/%Y",)
#     )
#     resume = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))
#     # role = forms.BooleanField(widget=forms.RadioSelect(attrs={'class': 'radio'}, choices=ROLE))
#
#     class Meta:
#         model = UserProfile
#         fields = [
#             'dob', 'gender', 'country', 'phone_number', 'student_number', 'school', 'program', 'start_program',
#             'complete_program', 'qualification', 'company_name', 'company_location', 'job_position',
#             'job_position_period_from', 'job_position_period_to', 'resume', 'profile_img', 'region'
#         ]
#
#
