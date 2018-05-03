# -*- coding: utf-8 -*-
from __future__ import unicode_literals
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

def logout_view(request):
	logout(request)
	return redirect('/')


def register_view(request):
	title ="Register"
	next = request.GET.get('next')
	form = UserRegistrationForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get("password")
		user.set_password(password)
		user.save()
		new_user = authenticate(username=user.username, password= password)
		login(request,new_user)
		if next:
			return redirect(next)
		return redirect('/')

	context ={
		"form":form,
		"title":title,
	}
	return render(request,"login.html",context)