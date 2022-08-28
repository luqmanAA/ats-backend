# from django import forms
from django.forms import CharField, ModelForm, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Comment

class CommentModelForm(ModelForm):
    description = CharField(widget=Textarea(attrs={'id':'description'}), label='')
    class Meta:
        model = Comment
        fields = ['description']
        
   
class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        )
   