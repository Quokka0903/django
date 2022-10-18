from django import forms
from .models import Movies


class MovieForm(forms.ModelForm):

    class Meta:
        model = Movies
        fields = '__all__'

        widgets = {
            'title' : forms.TextInput(attrs={'placeholder' : '세 얼간이'}),
            'director' : forms.TextInput(attrs={'placeholder' : '라지쿠마르 히라니'}),
            'comment' : forms.Textarea(attrs={'placeholder' : '나 얼간이 아니다!', 'rows' : '3px', 'cols' : '40px'}),
        }
