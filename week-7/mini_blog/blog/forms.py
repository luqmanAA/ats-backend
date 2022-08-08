# from django import forms
from django.forms import CharField, ModelForm, Textarea

from .models import Comment

class CommentModelForm(ModelForm):
    description = CharField(widget=Textarea(attrs={'id':'description'}), label='')
    class Meta:
        model = Comment
        fields = ['description']
        
   
    