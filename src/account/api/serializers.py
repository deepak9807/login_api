from rest_framework.serializers import (
	EmailField,
	CharField,
	ModelSerializer, 
	SerializerMethodField,
	ValidationError,
	)
from django.contrib.auth import get_user_model
# Import the User model
User = get_user_model()


class UserCreateAPISerializer(ModelSerializer):
	email = EmailField(label ='Email Address')
	email2 = EmailField(label= 'Confirm Email')
	class Meta:
		model = User 
		fields = [
			'username',
			'email',
			'email2',
			'password',
			
		]
		extra_kwargs = {"password":
							{"write_only":True},
						'email2':{"write_only":True}

					}
	# we are creating user and also vailidate email


	def validate_email2(self,value):
		data = self.get_initial()
		email1 = data.get('email')
		email2 = value
		if email2 != email1:
			raise ValidationError("Email should be match")

		qs = User.objects.filter(email=email2)
		if qs.exists():
			raise ValidationError("This user alredy exist")
		return value
	def create(self, validated_data):
		username = validated_data['username']
		email = validated_data['email']
		password = validated_data['password']
		user_obj = User(
				username = username,
				email = email
			)
		user_obj.set_password(password)
		user_obj.save()
		return validated_data

class UserLoginAPISerializer(ModelSerializer):
	token = CharField(allow_blank=True, read_only=True)
	email = EmailField(label= 'Email Address')
	class Meta:
		model = User 
		fields = [
			'email',
			'password',
			'token',
		]

	def validate(self,data):
		user_obj = None
		email = data.get('email',None)
		password = data["password"]
		if not email:
			raise ValidationError("An Email is required to login")
		user = User.objects.filter(email=email)
		if user.exists():
			user = user
		else:
			raise ValidationError("This user is not valid")
		if user_obj:
			if not user_obj.check_password(password):
				raise ValidationError("Incorrect credential please try again")
		data["token"] ="Some random token"

		return data




			