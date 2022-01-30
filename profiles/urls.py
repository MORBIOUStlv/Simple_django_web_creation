from  django.urls import path
from .views import my_profile_view, settings

#parameter for namespace
app_name = 'profiles'

urlpatterns = [
    path('myprofile/', my_profile_view, name='my-profile-view'),
    path('settings', settings, name='settings'),

]
