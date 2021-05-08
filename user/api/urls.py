

from django.urls import path
from user.api.views import RegisterUserAPI,LoginUserAPI


urlpatterns = [
    path('register/', RegisterUserAPI.as_view(), name='Register'),
    path('login/', LoginUserAPI.as_view(), name='Login'),



]