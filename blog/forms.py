from django import forms
from .models import Comment

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)
    
class CommentForm(forms.ModelForm):
    name = forms.CharField(
        label='Full name',
        widget=forms.TextInput(attrs={
            'class': 'oleez-input',
        })
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'oleez-input',
        })
    )
    body = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={
            'class': 'oleez-textarea',
        })
    )
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']