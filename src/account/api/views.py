from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
# Import the User model
from .serializers import (
	UserCreateAPISerializer,
	UserLoginAPISerializer,
	)

from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_406_NOT_ACCEPTABLE

User = get_user_model()

class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateAPISerializer
	queryset = User.objects.all()

class UserLoginAPIView(APIView):
	#permission_classes = (AllowAny,)
	serializer = UserLoginAPISerializer
	def post(self,request, *arg,**kwagrs):
		data = request.data
		serializer = UserLoginAPISerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			new_data = serializer.data
			return Response(new_data,status=HTTP_200_OK)
		return Response(serializer.error, status= HTTP_406_NOT_ACCEPTABLE)