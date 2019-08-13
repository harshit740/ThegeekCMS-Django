from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    required_css_class = 'is-danger'

    username = forms.CharField(max_length=30,required=False,widget=forms.TextInput(attrs={'placeholder': ' Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. '},))
    first_name = forms.CharField(max_length=30, required=True,widget=forms.TextInput(attrs={'placeholder': 'Enter your First name'}))
    last_name = forms.CharField(max_length=30, required=False,widget=forms.TextInput(attrs={'placeholder': 'Enter your Last name'}) )
    email = forms.EmailField(max_length=254, widget=forms.TextInput(attrs={'placeholder': ' Required. Inform a valid email address. '}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
