from django.conf import settings
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token

app_name = 'account'
from .views import UserCreateAPIView,UserLoginAPIView

urlpatterns = [
  	url(r'^api-token/', obtain_jwt_token),# generating Token for user to get access the api
    url(r'^api/register/', UserCreateAPIView.as_view(), name="register-api"), # for signUp the user
    url(r'^api/login/', UserLoginAPIView.as_view(), name="login-api"),# Login user account
]