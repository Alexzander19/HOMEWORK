from django.shortcuts import get_object_or_404, redirect, render

from .models import Services, Interested
from .forms import InterestForm

# Create your views here.

def index(request):
     return render(request,'itcompany\main\index.html')

def list(request):
     
     services = Services.objects.all()

     return render(request,'itcompany\list.html',{'services': services})

def interest(request, service_id):

# product = Product.objects.get(id = p_id)
    service = get_object_or_404(Services, id=service_id)
    

    if request.method != 'POST':
        # Исходный запрос. Создается новая форма
        form = InterestForm()
    else:
        # Отправка данных POST, обработать данные.
        form = InterestForm(data=request.POST)
        if form.is_valid():
            new_interest = form.save(commit=False)
            new_interest.service = service
            new_interest.save()
            return redirect('list')
        
    context = {'form': form, 'service': service}
    return render(request,'itcompany/interest.html',context)


