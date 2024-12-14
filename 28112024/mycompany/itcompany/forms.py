from django import forms
from .models import Interested

class InterestForm(forms.ModelForm):
    class Meta:
        model = Interested
        fields = ['name', 'phone', 'request']
        labels = {'name': 'Ваше имя: ', 'phone': 'Ваш телефон: ', 'request': 'Ваши пожелания: '}

        # service = models.ForeignKey(Services,on_delete=models.DO_NOTHING)
        # name = models.CharField(max_length=100)
        # phone = models.CharField(max_length=20)
        # request = models.TextField()
        # date_time_create = models.DateTimeField(auto_now_add=True)