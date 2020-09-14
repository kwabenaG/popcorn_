import datetime
import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

# third parties
from phonenumber_field.modelfields import PhoneNumberField
from PIL import Image


# Create your models here.
class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    GENDER = (
        ('Male', _('Male')),
        ('Female', _('Female')),
    )

    DEGREE = (
        (None, _('Select your degree')),
        ('Undergraduate', _('Undergraduate')),
        ('Bachelor', _('Bachelor')),
        ('Master', _('Master')),
        ('PhD', _('PhD')),
    )
    userCreated = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True,
                                       verbose_name='Registered User')
    # middle_initials = models.CharField(max_length=20, blank=True, null=True)
    dob = models.DateField(blank=True, null=True, verbose_name='Birth Date')
    gender = models.CharField(null=True, blank=True, max_length=100, choices=GENDER)
    country = models.CharField(blank=True, null=True, max_length=200)
    phone_number = PhoneNumberField(blank=True, null=True, unique=True)
    student_number = models.IntegerField(unique=True, null=True, verbose_name='access code', blank=True)
    school = models.CharField(null=True, blank=True, max_length=100, )
    program = models.CharField(max_length=100, null=True, blank=True,)
    start_program = models.DateField(null=True, blank=True, verbose_name='program_start')
    complete_program = models.DateField(null=True, blank=True, verbose_name='program_complete')
    qualification = models.CharField(blank=True, null=True, verbose_name='qualification', max_length=200,
                                     choices=DEGREE)
    profile_img = models.ImageField(default='profile_image.png', upload_to='profile_images/',
                                    verbose_name='Profile Image', null=True, blank=True)
    company_name = models.CharField(max_length=200, null=True, blank=True, verbose_name='company name')
    company_location = models.CharField(max_length=200, null=True, blank=True, verbose_name='company location')
    job_position = models.CharField(max_length=200, null=True, blank=True, verbose_name='job position')
    job_position_period_from = models.DateField(null=True, blank=True, verbose_name='job period from')
    job_position_period_to = models.DateField(null=True, blank=True, verbose_name='job period to')
    resume = models.FileField(verbose_name='Student Resume', null=True, blank=True, upload_to='resume_uploads/')
    region = models.CharField(blank=True, null=True, max_length=200)
    # role = models.CharField(blank=True, null=True, max_length=200)
    skills = models.CharField(blank=True, null=True, max_length=200)

    def __str__(self, **kwargs):
        return '{} Profile'.format(self.userCreated.username)

    # def get_absolute_url(self):
    #     return reverse('userprofile', args=[str(self.id)])
    # signal created here is moved to its own file
    # will add custom image crop sizing method here


class Reviews(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    reviews = models.CharField(blank=True, null=True, max_length=100,)



