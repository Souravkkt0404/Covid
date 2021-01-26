import re
from django.shortcuts import render
from django.http import HttpResponse
from app_one.models import *
import random
from bs4 import BeautifulSoup
from urllib.request import urlopen

def login_auth(request):
	un = request.POST.get('uname') #cricket
	pw = request.POST.get('pword') #pgd123
	x = user_details.objects.values_list('username',flat=True)
	y = user_details.objects.values_list('password',flat=True)
	if(un in x):
		if(pw in y):
			for i in user_details.objects.values_list():
				if( (un == i[0]) and (pw == i[1]) ):
					return render(request,'home.html')
					break
				else:
					continue
		else:
			return render(request,'login.html',{'error':"Wrong credentials!!"})
	else:
		return render(request,'login.html',{'error':"Wrong credentials!!"})
	return render(request,'login.html',{'error':"Wrong credentials!!"})

def login(request):
	return render(request,'login.html')

def reg(request):
	return render(request,'reg_form.html')

def covid(request):
	return render(request,'covid.html')

def index(request):
	return render(request,'index.html')

def register(request):
	un = request.POST.get('uname')
	pw = request.POST.get('pword')
	cpw = request.POST.get('cpword')
	validate_pass(pw)
	user_list = user_details.objects.values_list('username',flat=True)
	if un in user_list:
		return render(request,'reg_form.html',{'error':"Username already exists"})
	else:
		if pw == cpw:
			a = user_details(username=un,password=pw)
			a.save()
			return render(request,'reg_form.html',{'msg':"Registration Successful!!"})
		else:
			return render(request,'reg_form.html',{'error':"Password entered are not correct"})

def validate_pass(pw):
	if(len(pw)>=8):
		if(re.search("[a-z]",pw) and re.search("[A-Z]",pw)) and (re.search("[0-9]",pw)):
			print("correct format")
		else:
			print("Not in required format")
	else:
			print("Too small, minimum of 8 character required")

def test_return(request):
	return render(request,'ws_home.html')

def login_ws(request):
	return render(request,'login_new.html')

def login_validation(request):
	un = request.POST.get('uname') #surana
	pw = request.POST.get('psw') #pgd123
	x = User_table.objects.values_list('username',flat=True)
	y = User_table.objects.values_list('password',flat=True)
	if (un in x):
		if (pw in y):
			for i in User_table.objects.values_list():
				if((un == i[0]) and (pw == i[1]) ):
					request.session['username'] = un
					return render(request,'ws_home.html',{'user':un})
				else:
					continue
		else:
			return render(request,'login_new.html',{'error':"Wrong credentials!!"})
	else:
		return render(request,'login_new.html',{'error':"Wrong credentials!!"})
	return render(request,'login_new.html',{'error':"Wrong credentials!!"})

def logout(request):
	del request.session['username']
	return render(request,'login.html',{'logout_msg':'You are logged out of the page!!'})