from django.shortcuts import  get_object_or_404, redirect, render
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.contrib import messages
from .forms import SignUpForm,UpdateUserForm, UpdateUserProfileForm,PostForm
from .models import Profile, Post, User, Subscribers, Follow, Comment, Like
from .emails import send_welcome_email
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.decorators import login_required

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
@login_required(login_url='login')
def profile(request,username):
    images = request.user.profile.posts.all()
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    contex = {
        'user_form': user_form,
        'prof_form': prof_form,
        'images': images,

    }
    return render(request, 'accounts_pages/profile.html', contex)

@login_required(login_url='login')
def user_profile(request,username):
    profile_user=get_object_or_404(User,username=username)
    if request.user == profile_user:
        return redirect('profile',username=request.user.username)
    user_posts=profile_user.profile.posts.all()

    followers=Follow.objects.filter(followed=profile_user.profile)  
    following=None
    for follower in followers:
        if request.user.profile == follower.follower:
            following=True  
        else:
            following=False
    context = {
        'profile_user':profile_user,
        'user_posts':user_posts,
        'followers':followers,
        'following':following
        }
    return render(request, 'accounts_pages/user_profile.html', context)
            
@login_required(login_url='login')
# def index(request):
#     images = Post.objects.all()
#     comments = Comment.objects.all()
#     users = User.objects.exclude(id=request.user.id)
#     if request.method == "POST":
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             image = form.save(commit = False)
#             image.user = request.user.profile
#             image.save()
#             messages.success(request, f'Successfully uploaded your pic!')
#             return redirect('index')
#     else:
#         form = PostForm()
#     return render(request, 'index.html', {"images":images[::-1], "form": form, "users": users, "comments": comments })
def post(request):
    images = Post.objects.all()
    users = User.objects.exclude(id=request.user.id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user.profile
            post.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = PostForm()
    params = {
        'images': images,
        'form': form,
        'users': users,

    }
    return render(request, 'index.html', params)
