from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, ProfileForm, LoginForm
from .models import Profile
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount

def home(request):
    return render(request, 'user/home.html')

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            
            profile = Profile.objects.get(user=user)
            profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
            profile_form.save()

            return redirect('login')

    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileForm()
        context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'user/register.html', context)

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                form.add_error(None, 'Invalid email or password')
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form': form})

@login_required(login_url='login')
def profile(request):
    social_account = SocialAccount.objects.filter(user=request.user).first()
    return render(request, 'user/profile.html', {'user': request.user, 'profile': request.user.profile, 'social_account': social_account})

