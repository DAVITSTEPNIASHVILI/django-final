from django import forms
from .models import Post

class AddPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('description',)
        widgets = {
            'description': forms.TextInput({
                'style': 'height: 150px; margin-bottom: 30px;'
            })
        }