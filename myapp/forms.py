from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Post


class SignUpForm(UserCreationForm):
    email=forms.EmailField(max_length=254,help_text='Required.inform a valid email address')
    class Meta:
        model=User
        fields=('username','email','password1','password2')

# class PickForm(ModelForm):
#     class Meta:
#         model = Car        
# class SignUpForm(UserCreationForm):
# 	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
# 	first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
# 	last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
	

# 	class Meta:
# 		model = User
# 		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


# 	def __init__(self, *args, **kwargs):
# 		super(SignUpForm, self).__init__(*args, **kwargs)

# 		self.fields['username'].widget.attrs['class'] = 'form-control'
# 		self.fields['password1'].widget.attrs['class'] = 'form-control'
# 		self.fields['password2'].widget.attrs['class'] = 'form-control'

class UpdateUserForm(forms.ModelForm):
    email=forms.EmailField(max_length=254,help_text='Required.inform a valid email address')
    class Meta:
        model=User
        fields=('username','email')

class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        models=Profile
        fields=('name','profile_pic','bio','location')
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image_post', 'caption')