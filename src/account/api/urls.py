from django.conf import settings
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token

app_name = 'account'
from .views import UserCreateAPIView

urlpatterns = [
  	url(r'^api/login/', obtain_jwt_token),# generating Token for user to get access the api
    url(r'^api/register/', UserCreateAPIView.as_view(), name="register-api"), # for signUp the user
]