import uuid
import datetime

from django.db import models
from django.urls import reverse

from phonenumber_field.modelfields import PhoneNumberField

from accounts.models import CustomUser  # default user


#  skill required
class SkillNeeded(models.Model):
    skill_name = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Skills Required'

    def __str__(self):
        return self.skill_name


# tags model
class Tags(models.Model):
    # remember to add uuid as  the id
    tag_name = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.tag_name

    def get_absolute_url(self, *args):
        return reverse('tags', args=[str(self.tag_name)])


# general offers for all
class Offers(models.Model):
    JOB_TYPE = (
        (None, 'Select Job Type'),
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Internship', 'Internship')
    )

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    offer_name = models.CharField(max_length=200, verbose_name='Offer Name', blank=True)
    offer_type = models.CharField(max_length=200, verbose_name='Offer Type', blank=True, null=True, choices=JOB_TYPE)
    offer_job_name = models.CharField(max_length=200, blank=True, null=True, default='Software Developer')
    offer_number = models.IntegerField(verbose_name='Offer number', blank=True, null=True)
    offer_description = models.TextField()
    company_name = models.CharField(max_length=200, verbose_name='Company Name', blank=True, null=True)
    company_description = models.TextField()
    offer_location = models.CharField(max_length=200, verbose_name='Offer Location', blank=True, null=True)
    offer_phone_number = PhoneNumberField(blank=True, null=True, unique=True)
    offer_status = models.IntegerField(verbose_name='Offer Status', blank=True, null=True)
    offer_min_max_limit = models.IntegerField(verbose_name='Offer Intake', blank=True, null=True)
    offer_date_created = models.DateTimeField(verbose_name='Offer Date')
    offer_date_updated = models.DateTimeField(verbose_name='Offer Date Updated', auto_now=True)
    offer_tag = models.ManyToManyField(Tags)  # tag model field
    skill_qualified_offer = models.ManyToManyField(SkillNeeded)
    user_interested = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Offers'

    def __str__(self):
        return self.offer_name


class QuickContact(models.Model):
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True, unique=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = 'Quick Contact'

    def __str_(self):
        return format(self.first_name, self.email)

    def get_absolute_url(self):
        return reverse('quick-contacts', args=[str(self.first_name)])


# offer form model for the offer request from user
class ApplyForm(models.Model):
    user_who_applied = models.CharField(max_length=200, blank=True, null=True)
    offer_selected = models.CharField(max_length=200, blank=True, null=True)
    offer_name = models.CharField(max_length=200, blank=True, null=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True, unique=True)
    user_phone_number = PhoneNumberField(blank=True, null=True, unique=True)
    # resume = models.FileField(verbose_name='resume', upload_to='popcorn/resume', blank=True)
    apply_job_date = models.DateTimeField(auto_now_add=True, verbose_name='Apply Job Date Time')

    class Meta:
        verbose_name_plural = 'Apply User Form'

    def __str__(self):
        return '{} {} offer'.format(self.last_name, self.offer_name)

    def get_absolute_url(self):
        return reverse('apply-form', args=[str(self.id)])


# user resume file
class UserResumeFile(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_query_name='real_user',
                                related_name='real_user')
    offer_id = models.ForeignKey(Offers, max_length=200, on_delete=models.CASCADE,
                                 related_query_name='offer_resume_user', related_name='offer_resume_user')
    file_name = models.FileField(max_length=200, verbose_name='User File Name', blank=True, null=True)
    date_created = models.DateTimeField(verbose_name='Date Created', auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name='Date Updated', auto_now_add=True)

    def __str__(self):
        return '{} {}'.format(self.offer_id.offer_number, self.file_name)

    def get_absolute_url(self):
        return reverse('apply-form', args=[str(self.id)])


# request offer models
class RequestOffers(models.Model):
    request_offer = models.ForeignKey(Offers, on_delete=models.CASCADE,
                                      related_name='request_offer_from_client',
                                      related_query_name='request_offer_from_client')
    offer_name = models.CharField(max_length=200, blank=True, null=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True, unique=True)
    user_phone_number = PhoneNumberField(blank=True, null=True, unique=True)
    # resume = models.FileField(verbose_name='resume', upload_to='popcorn/resume', blank=True)


# job alerts model

class JobAlert(models.Model):
    full_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    date_joined_alert = models.DateTimeField(verbose_name='Date Subscribed', auto_now_add=True)
