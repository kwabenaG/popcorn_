# offer forms

from django.contrib.auth.forms import forms
from django.core.validators import FileExtensionValidator, RegexValidator, EmailValidator

from phonenumber_field.formfields import PhoneNumberField
from .models import Offers, ApplyForm, JobAlert
from accounts.models import CustomUser


class OfferForm(forms.ModelForm):
    JOB_TYPE = (
        (None, 'Select Job Type'),
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Internship', 'Internship')
    )

    offer_name = forms.CharField(widget=forms.TextInput())
    offer_number = forms.IntegerField(widget=forms.TextInput())
    offer_type = forms.SelectMultiple(choices=JOB_TYPE, )
    offer_description = forms.CharField(widget=forms.TextInput(attrs={}))
    company_name = forms.CharField(widget=forms.TextInput(attrs={}))
    company_description = forms.CharField(widget=forms.TextInput(attrs={}))
    offer_phone_number = PhoneNumberField()
    offer_location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control floating'}))
    offer_status = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control floating'}))
    offer_min_max_limit = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control floating'}))
    offer_date_created = forms.DateField(input_formats="'%d/%m/%Y'",
                                         widget=forms.DateInput(format="'%d/%m/%Y'", attrs={}))
    offer_date_update = forms.DateTimeField(input_formats="'%d/%m/%Y'",
                                            widget=forms.DateTimeInput(format="'%d/%m/%Y'", attrs={}))

    class Meta:
        model = Offers
        fields = [
            'offer_name', 'offer_number', 'company_name', 'offer_location', 'offer_status',
            'offer_min_max_limit', 'offer_date_created', 'offer_phone_number', 'offer_type',
            'company_description', 'offer_description', 'offer_date_update'
        ]


# offer request form
class OfferRequestForm(forms.ModelForm):

    alphaVal = RegexValidator(r'^[a-zA-Z ]+$', 'Only letters allowed')
    emailVal = EmailValidator('Enter a valid email. Oops...')

    offer_selected = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={'class': 'utf-with-border', 'required': True}))

    offer_name = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={'class': 'utf-with-border', 'required': 'required'}))

    first_name = forms.CharField(max_length=200, validators=[alphaVal],
                                 widget=forms.TextInput(
                                     attrs={'class': 'utf-with-border', 'placeholder': 'First Name',
                                            'required': 'required', 'id': 'first_name'}))

    last_name = forms.CharField(max_length=200, validators=[alphaVal],
                                widget=forms.TextInput(
                                    attrs={'class': 'utf-with-border', 'placeholder': 'Last Name',
                                           'required': 'required', 'id': 'last_name'}))

    phone_number = PhoneNumberField()

    email = forms.CharField(max_length=200, validators=[emailVal], widget=forms.TextInput(
        attrs={'class': 'utf-with-border', 'placeholder': 'Email',
               'required': 'required'}))
    user_who_applied = forms.BooleanField(widget=forms.TextInput(
        attrs={'class': 'utf-with-border',
               'required': 'required'}))

    # user_resume = forms.FileField(validators=[FileExtensionValidator(['pdf', 'doc', 'docx'])],
    #                               widget=forms.FileInput(attrs={'class': 'utf-with-border'}))

    class Meta:
        model = ApplyForm
        fields = [
            'first_name', 'last_name', 'offer_name', 'phone_number', 'email', 'offer_selected', 'user_who_applied'
        ]
        # field = '__all__'


class JobAlertForm(forms.ModelForm):
    alphaVal = RegexValidator(r'^[a-zA-Z ]+$', 'Only Letters Allowed. Oops.')
    emailVal = EmailValidator('Enter a valid email. Oops.')
    full_name = forms.CharField(max_length=200, validators=[alphaVal],
                                widget=forms.TextInput(
                                    attrs={'class': 'utf-with-border', 'placeholder': 'Full Name Eg. George Addo',
                                           'required': 'required', 'id': 'full_name' }))
    email = forms.CharField(max_length=200, validators=[emailVal],
                            widget=forms.TextInput(
                                attrs={'class': 'utf-with-border', 'placeholder': 'Email  eg. george@gmail.com',
                                       'required': 'required', 'id': 'email'}))

    class Meta:
        model = JobAlert
        fields = [
            'full_name', 'email'
        ]
