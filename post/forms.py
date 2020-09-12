from django import forms
from django.contrib.auth.models import User
from .models import Post

#####################################################################################################
#       auth forms                                                                                  #
#####################################################################################################
class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets={
            'password': forms.PasswordInput(),
        }

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())

#####################################################################################################
#       Post Forms                                                                                  #
#####################################################################################################

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ["auther"]

