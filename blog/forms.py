from .models import Comment
from django import forms
from .models import CollaborateRequest
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


# COLLABORATE REQUEST FORM

class CollaborateForm(forms.ModelForm):
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')
        # widgets = {
        #   'email': forms.EmailInput(attrs={'class': 'primary'}),
        # }