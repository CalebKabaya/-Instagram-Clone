from django.shortcuts import  redirect, render
from django.http import HttpResponse, Http404
from django.contrib import messages
from .forms import SignUpForm,UserCreationForm
from .models import Profile, Post, User, Subscribers, Follow, Comment, Like
from .emails import send_welcome_email
from django.contrib.auth import authenticate, login, logout
from .models import *


from django.contrib import messages


# Create your views here.


# Create your views here.
def welcome(request):
    return render(request,'index.html')


# def register(request):
#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             email = form.cleaned_data['email']
#             messages.success(request, f'Successfully created account created for {username}! Please log in to continue')
#             return redirect('login')
#     else:
#         form = SignUpForm()
#     return render(request, 'users/register.html', {'form':form})    


# def register(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('login')
#     else:
#         form = SignUpForm()
#     return render(request, 'users/register.html', {'form':form}) 

# def login(request):

#         return render(request, 'users/login.html',) 

# def register(request):
# 	if request.user.is_authenticated:
# 		return redirect('welcome')
# 	else:
# 		form = SignUpForm()
# 		if request.method == 'POST':
# 			form = SignUpForm(request.POST)
# 			if form.is_valid():
# 				form.save()
# 				user = form.cleaned_data.get('username')
# 				messages.success(request, 'Account was created for ' + user)

# 				return redirect('login')
			

# 		context = {'form':form}
# 		return render(request, 'users/register.html', context)



# def loginPage(request):
# 	if request.user.is_authenticated:
# 		return redirect('welcome')
# 	else:
# 		if request.method == 'POST':
# 			username = request.POST.get('username')
# 			password =request.POST.get('password')

# 			user = authenticate(request, username=username, password=password)

# 			if  user is not None:
# 				login(request, user)
# 				return redirect('welcome')
# 			else:
# 				messages.info(request, 'Username OR password is incorrect')

# 		context = {}
# 		return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')



def login_page(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('welcome')
		else:
			messages.success(request, ("There Was An Error Logging In, Try Again..."))	
			return redirect('login')	


	else:
		return render(request, 'users/login.html', {})


def register(request):
	if request.method == "POST":
		form =SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ("Registration Successful!"))
			return redirect('welcome')
	else:
		form = SignUpForm()

	return render(request, 'users/register.html', {
		'form':form,
		})