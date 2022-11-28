from .models import articles, Comments
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from django import forms


class articles_form(ModelForm):
    class Meta:
        model = articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            }),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('text',)
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['text'].widget = Textarea(attrs={'rows':5})

    