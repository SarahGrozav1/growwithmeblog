from .models import Comment
from django import forms
from .models import CollaborateForm
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


# COLLABORATE REQUEST FORM

class CollaborateRequestForm(forms.ModelForm):
    class Meta:
        model = CollaborateForm
        fields = ('name', 'email', 'message')