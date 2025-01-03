from allauth.socialaccount.signals import social_account_added
from django.dispatch import receiver
from .models import Profile

@receiver(social_account_added)
def populate_profile(sociallogin, **kwargs):
    if sociallogin.account.provider == 'github':
        user = sociallogin.user
        profile, created = Profile.objects.get_or_create(user=user)
        profile.profile_image = sociallogin.account.extra_data.get('avatar_url', '')
        profile.address = sociallogin.account.extra_data.get('location', 'Unknown')
        profile.save()