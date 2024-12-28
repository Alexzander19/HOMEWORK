from django import forms
from .models import Movie, Session

class MovieAddForm(forms.ModelForm):
  class Meta:
    model = Movie
    fields = ['title', 'duration', 'genre', 'release_date','description']
    labels = {'duration': 'продолжительность фильма (мин.)',
              'genre': 'жанр фильма'}
 
    widgets = {  
      
     'title': forms.TextInput(attrs={
        'class': 'form-control',
        # 'id': 'floatingTitle',
        # 'placeholder': 'Очень простая задача',
        'required': True
      }),
      
      'release_date': forms.DateInput(attrs={
        'class': 'form-control',
        'id': 'floatingDueDate',
        'type': 'date',
        'required': True

      }),
      'description': forms.TextInput(attrs={
        'class': 'form-control',
        # 'id': 'floatingDescription',
        # 'placeholder': 'Нужно сделать несколько пунктов...',
        # 'required': True
      }),
    }


class SessionAddForm(forms.ModelForm):
  class Meta:
    model = Session
    fields = ['movie', 'hall', 'show_time', 'price']
 
    widgets = {  
      
      'show_time': forms.TimeInput(attrs={
        'class': 'form-control',
        'id': 'floatingDueDate',
        'type': 'time',
        'required': True

      }),
      
    }
