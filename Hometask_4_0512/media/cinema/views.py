from django.shortcuts import render
from .models import Session

# Create your views here.

def sessions(request):
    sessions = Session.objects.all()
    return render(request,'cinema\sessions.html',context={'sessions': sessions})

def index(request):
    return render(request,'cinema\index.html')
