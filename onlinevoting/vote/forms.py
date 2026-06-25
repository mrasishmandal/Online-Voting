from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Vote

# Form for user registration with email field included
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email'] # Built-in form handles passwords automatically

# Form for casting a vote by selecting a candidate
class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ['candidate']