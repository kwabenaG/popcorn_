# views.py
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.template import loader

# local files
from .forms import UpdateUserForm, UpdateProfileForm
from .models import CustomUser, UserProfile


def send_mail_to(request, *args, **kwargs):
    send_response_mail = send_mail(**kwargs)
    return send_response_mail


@login_required(login_url='account_login')
def user_profile(request, *args):
    user_profile_data = UserProfile.objects.filter(userCreated=request.user).first()
    user_forms = UpdateUserForm(instance=request.user)
    profile_forms = UpdateProfileForm(instance=user_profile_data)
    context = {'user_profile_data': user_profile_data, 'user_data': user_forms, 'profile_form': profile_forms}
    return render(request, 'account/profile/edit_user_profile.html', context)


# responsible for user edit algorithm
def edit_user_profile(request):
    user_profile_data = UserProfile.objects.filter(userCreated=request.user).first()
    if request.method == 'POST':
        # return HttpResponse('POSTed')
        user_forms = UpdateUserForm(request.POST, instance=request.user)
        profile_forms = UpdateProfileForm(request.POST, request.FILES, instance=user_profile_data)

        if user_forms.is_valid() and profile_forms.is_valid():
            user_forms.save()  # saves user data
            profile_forms.save()  # saves user profile data

            # add message
            messages.success(request, 'User Profile Updated Successfully!')

            # send mail
            # html message to the template
            html_message = loader.render_to_string('emails_temp/update_user_profile.html', context={
                'first_name': user_forms.cleaned_data.get('first_name'),
                'last_name': user_forms.cleaned_data.get('last_name')
            })
            send_mail_to(request, subject='User Profile Update', from_email='no-reply@popcorn.com',
                         recipient_list=[user_forms.cleaned_data.get('email')], html_message=html_message)  #  custom function returned send_mail

            return redirect('home_dashboard')
        else:
            # print out the error to the current form
            print(user_forms.errors)
            print(profile_forms.errors)
            user_forms = UpdateUserForm(instance=request.user)
            profile_forms = UpdateProfileForm(instance=user_profile_data)
            context = {'user_forms': user_forms, 'profile_forms': profile_forms, 'user_profile_data': user_profile_data}

            return render(request, 'account/profile/edit_user_profile.html', context)
    else:  # thus a GET request
        user_forms = UpdateUserForm(instance=request.user)
        profile_forms = UpdateProfileForm(instance=user_profile_data)
        context = {'user_forms': user_forms, 'profile_forms': profile_forms, 'user_profile_data': user_profile_data}
        return render(request, 'account/profile/edit_user_profile.html', context)

# def update_user_profile(request):
#     user_profile_data = UserProfile.objects.filter(userCreated=request.user).first()
#     if request.method == 'POST':
#         user_forms_update = UpdateUserForm(request.POST, instance=request.user)
#         userprofile_forms_update = UpdateProfileForm(request.POST, request.FILES)
#         if user_forms_update.is_valid() and userprofile_forms_update.is_valid():
#             user_forms_update.save()
#             userprofile_forms_update.save()
#             return HttpResponse('not working')
#         else:
#             print(user_forms_update.errors)
#             print(userprofile_forms_update.errors)
#             user_forms_update = UpdateUserForm(instance=request.user)
#             userprofile_forms_update = UpdateProfileForm()
#             context = {
#                 'user_forms_update': user_forms_update , 'userprofile_forms_update': userprofile_forms_update
#             }
#             return render(request, 'content/profile/edit_profile.html', context)
#     else:
#         user_forms_update = UpdateUserForm()
#         userprofile_forms_update = UpdateProfileForm()
#         return render(request, 'content/profile/edit_profile.html',
#                       {'user_forms_update': user_forms_update},
#                       {'userprofile_forms_update': userprofile_forms_update})

        # print(userprofile_forms_update)
        # return redirect('edit_userprofile')
        # print(user_forms_update)
        # print(userprofile_forms_update)
        # return HttpResponse('IT WORKED')

























# class based views would be revisited later
# class ProfileView(ListView):
#     # template_name = 'accounts/userprofile_list.html'
#     model = UserProfile
#     context_object_name = 'profile_list'
#     form = UpdateProfileForm
#
#
# class UpdateUserProfile(ListView):
#     form_class = [UpdateUserForm(), UpdateProfileForm()]
#     model = [UserProfile, CustomUser]
#     template_name = 'account/update_profile_list.html'
#     context_object_name = {'form': form_class}



