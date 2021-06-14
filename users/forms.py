from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
	email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'placeholder':'Email'}))
	first_name = forms.CharField(max_length=30, required=False, label='First Name', widget=forms.TextInput(attrs={'placeholder':'First Name'}))
	last_name = forms.CharField(max_length=30, required=False, label='Last Name', widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
	password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
	username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'placeholder':'Username'}))
	password2 = forms.CharField(label='Password Confirmation',widget=forms.PasswordInput(attrs={'placeholder':'Confirmation'}))
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']