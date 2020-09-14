# dir pages.views
import json
import sweetify

from django.http import JsonResponse
from django.core.serializers import serialize
from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.core.mail import send_mail
from django.template import loader

from offer.models import Offers, Tags, SkillNeeded  # from offers
from accounts.models import CustomUser
from offer.forms import OfferRequestForm, JobAlertForm


def home_page_view(request):
    # add try and catch exceptions
    all_offers = Offers.objects.all()  # GET all uploaded offers
    context = {'all_offers': all_offers}
    return render(request, 'popcorn/index/index.html', context)


# job listings from categories
def education_training(request):
    typeLevel = 'Education'
    context = {'typeLevel': typeLevel}
    return render(request, 'popcorn/index/listing_index.html', context)


def accounting_finance(request):
    typeLevel = 'Accounting / Finance'
    context = {'typeLevel': typeLevel}
    return render(request, 'popcorn/index/listing_index.html', context)


def human_resource(request):
    typeLevel = 'Human Resource'
    context = {'typeLevel': typeLevel}
    return render(request, 'popcorn/index/listing_index.html', context)


def telecom(request):
    typeLevel = 'Telecom'
    context = {'typeLevel': typeLevel}
    return render(request, 'popcorn/index/listing_index.html', context)


# get offer details
def display_latest_offer_details(request, offer_type_id):
    user = request.user.pk
    all_job_offers = Offers.objects.all()  # responsible for jobs other people viewed
    tag_cloud = Tags.objects.all()  # get tag clouds
    offer_request_offer = OfferRequestForm()  # get offer request forms
    job_alert_form = JobAlertForm()  # for job alerts
    offer_detail = get_object_or_404(Offers, id=offer_type_id)  # GET all uploaded offers
    skills = SkillNeeded.objects.filter(offers__skill_qualified_offer=offer_type_id)

    context = {'current_user': user, 'offer_detail': offer_detail, 'jobs_viewed': all_job_offers,
               'offer_applyForm': offer_request_offer, 'job_alerts': job_alert_form,
               'tag_cloud': tag_cloud}

    return render(request, 'popcorn/offer_details/details_index.html', context)


# post job or offer request to admin
@login_required(login_url="account_login")
def send_offer_request(request):
    response_data = {}
    if request.user.is_authenticated:
        if request.is_ajax() and request.method == 'POST':
            request_form = OfferRequestForm(request.POST)
            # request_form.applied_bool = 1  # inserts value of 1 to the  user model as 'has applied for the job'
            if request_form.is_valid():
                offer_selected = request_form.cleaned_data['offer_selected']
                offer_name = request_form.cleaned_data['offer_name']
                last_name = request_form.cleaned_data['last_name']
                first_name = request_form.cleaned_data['first_name']
                email = request_form.cleaned_data['email']
                phone_number = request_form.cleaned_data['phone_number']
                form_data = {'offer_name': offer_name, 'first_name': first_name, 'last_name': last_name,
                             'emails': email, 'offer_selected_by_user': offer_selected,
                             'phone_number': '{}{}'.format(phone_number.country_code, phone_number.national_number)}
                # print(form_data)
                request_form.save()
                # sweetify.success(request, 'Popcorn is great', text='Application sent successfully',  button="ok")
                messages.success(request, 'Application sent successfully')
                # save data to database
                response_data['success_message'] = 'Application Submitted Successfully. Thank You'

                # send emails to user
                html_message = loader.render_to_string('emails_temp/offer_apply_email.html', context={
                    'first_name': first_name,
                    'last_name': last_name
                })
                send_mail('Offer Notification', '',
                          'sales@popcorn.com', [request.user.email], html_message=html_message)

                return HttpResponse(json.dumps(response_data), content_type='application/json')
                # return JsonResponse(form_data, safe=False)
            else:
                form_errors = request_form.errors
                # print(form_errors)
                response_data['error_msg'] = '{0}'.format(form_errors)
                return HttpResponse(json.dumps(response_data), content_type='application/json')
        return redirect('homepage')


# get alert view - controller
def get_job_alerts(request):
    # if request.user.is_authenticated:
    alert_data = {}
    if request.is_ajax() and request.method == 'POST':
        alert_job_form = JobAlertForm(request.POST)
        if alert_job_form.is_valid():
            full_name = alert_job_form.cleaned_data['full_name']
            email = alert_job_form.cleaned_data['email']
            # save user form
            alert_data['success_msg_alert'] = 'Forms Submitted. Intern Alert Subscribed'
            # send mail to user
            html_msg = loader.render_to_string('emails_temp/job_alert_email.html', context={
                'full_name': full_name,
                'email': email

            })
            send_mail('Alert Subscription Notification', '', 'alerts@popcorn.com', [email], html_message=html_msg)
            return HttpResponse(json.dumps(alert_data), content_type='application/json')
        else:
            alert_job_errors = alert_job_form.errors
            alert_data['error_msg_alert'] = '{0}'.format(alert_job_errors)
            return HttpResponse(json.dumps(alert_data), content_type='application/json')
