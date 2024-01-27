from .models import Comment
from django import forms
from .models import CollaborateRequest
from django import forms


class CommentForm(forms.ModelForm):
    """
    Comment form for the user 
    """
    class Meta:
        model = Comment
        fields = ('body',)


# COLLABORATE REQUEST FORM

class CollaborateForm(forms.ModelForm):
    """
    An collaboration form
    """
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')
