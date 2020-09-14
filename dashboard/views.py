from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required


@login_required(login_url='account_login')
def dashboard_home(request):
    if request.user.groups == 'is_staff':
        return HttpResponse('ONLY FOR STAFFERS')
    return render(request, 'popcorn_dashboard/d_index.html')


@login_required(login_url='account_login')
def manage_jobs(request):
    return HttpResponse('ITS WORKING.....')


@login_required(login_url='account_login')
def manage_resume(request):
    return HttpResponse('ITS WORKING.....')


@login_required(login_url='account_login')
def reviews(request):
    return HttpResponse('ITS WORKING.....')
