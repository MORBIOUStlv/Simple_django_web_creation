from django.shortcuts import render
from .models import Profile
from .form import ProfileModelForm
# Create your views here.

def my_profile_view(request):
    profile = Profile.objects.get(user=request.user)
    profile_form = ProfileModelForm(request.POST or None, request.FILES or None)
    confirm = False

    if request.method == 'POST':
        if profile_form.is_valid():
            profile_form.save()
            confirm = True

    context = {
        'profile':profile
    }

    return render(request, 'profiles/main.html', context)


def settings(request):
    return render(request, 'profiles/settings.html')