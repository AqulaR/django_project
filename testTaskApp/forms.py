from django import forms
from .models import *

class CommentForm(forms.ModelForm):
    task_id = forms.IntegerField(widget=forms.HiddenInput())
    text = forms.CharField(
        label='', 
        widget=forms.TextInput(attrs={'placeholder': 'Напишите коментарий'})
    )
    class Meta:
        model = Comments
        fields = ['text']
        
class PrCommentForm(forms.ModelForm):
    text = forms.CharField(
        label='', 
        widget=forms.TextInput(attrs={'placeholder': 'Напишите коментарий'})
    )
    class Meta:
        model = PrComments
        fields = ['text']