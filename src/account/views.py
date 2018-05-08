# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
import json
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)
from django.shortcuts import render,redirect,get_object_or_404
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth import get_user_model
# Create your views here.
User = get_user_model()
def home_view(request):
	title = "Home"
	context = {
	'title':title, 
	}
	return render(request, "home.html", context)

# Login the user
def login_view(request):
	Login = "Login"
	next = request.GET.get('next')
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username, password= password)
		login(request,user)
		if next:
			return redirect(next)
		return redirect('/')
	return render(request,"login.html",{"form":form, "title":Login})
# logout the user 
def logout_view(request):
	logout(request)
	return redirect('/')

def register_view(request):
	title ="Register"
	form = UserRegistrationForm(request.POST or None)
	if form.is_valid():
		# Here I am using Register api 
		url = "http://127.0.0.1:8000/api/register/"
		username = form.cleaned_data.get("username")
		email = form.cleaned_data.get("email")
		email2	 = form.cleaned_data.get("email2")
		password = form.cleaned_data.get("password")
		url = "http://127.0.0.1:8000/api/register/"
		data = {
		        "username": username,
		        "email": email,
		        "email2": email2,
		        "password": password,

		}
		data_json = json.dumps(data)
		headers = {'Content-type': 'application/json'}
		response = requests.post(url, data=data_json, headers=headers)
		print(response.status_code)
		if response.status_code == 201:
			# Authenticate the user 
			new_user = authenticate(username=username, password= password)
			# login the user after athenticate
			login(request,new_user)
			return redirect('/')
	context ={
		"form":form,
		"title":title,
	}
	return render(request,"login.html",context)

# Here I am using Form to store the register data
# def register_view(request):
# 	title ="Register"
# 	next = request.GET.get('next')
# 	form = UserRegistrationForm(request.POST or None)
# 	if form.is_valid():
# 		user = form.save(commit=False)
# 		password = form.cleaned_data.get("password")
# 		user.set_password(password)
# 		user.save()
# 		new_user = authenticate(username=user.username, password= password)
# 		login(request,new_user)
# 		if next:
# 			return redirect(next)
# 		return redirect('/')

# 	context ={
# 		"form":form,
# 		"title":title,
# 	}
# 	return render(request,"login.html",context)