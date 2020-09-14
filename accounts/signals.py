
from .models import UserProfile
from django.dispatch import receiver  # for decorator purposes and event listener
# from django.contrib.auth import get_user_model

# third parties (allauth)
from allauth.account.signals import user_signed_up  # from all auth


# automatically add the user profile details to all newly registered user
@receiver(user_signed_up)
def create_user_profile(request, **kwargs):
    user = kwargs['user']
    profile = UserProfile(userCreated=user)
    profile.save()
    return profile
