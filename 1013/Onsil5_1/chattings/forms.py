from django import forms
from .models import Chat


class ChatForm(forms.ModelForm):

    class Meta:
        model = Chat
        fields = '__all__'

        widgets = {
            'user' : forms.TextInput(attrs={'placeholder' : 'Nickname'}),
            'content' : forms.Textarea(attrs={'placeholder' : 'Chat!'}),
        }
