from django.shortcuts import redirect, render
from .models import Session, Ticket

# Create your views here.

def sessions(request):
    sessions = Session.objects.all().order_by('show_time')
    return render(request,'cinema\sessions.html',context={'sessions': sessions})

def index(request):
    return render(request,'cinema\index.html')

def sessions_in_hall(request,hall_id):
    sessions = Session.objects.filter(hall_id=hall_id).order_by('show_time')
    hall_name = sessions[0].hall.name

    tickets_num = []
    free_seat = []

    for session in sessions:
        # здесь было бы уместно сравнить количество бкупленных билетов с вместимостью зала
        num = len(Ticket.objects.filter(session=session))
        tickets_num.append(num)
        if num < session.hall.capacity:
            free_seat.append(True)
        else:
            free_seat.append(False)
    
    # в html pop выводит и удаляет последний элемент, поэтому:
    tickets_num.reverse()
    free_seat.reverse()

    
    context={'sessions': sessions, 'hall_name': hall_name, 'tickets_num': tickets_num, 'free_seat': free_seat}

    return render(request,'cinema\sessions_in_hall.html',context=context)

def by_ticket(request,session_id):

    session = Session.objects.get(id=session_id)
    ticket = Ticket.objects.create(session=session)

    return redirect('in_hall',session.hall_id)

def tickets_sold(request):
    sessions = Session.objects.all().order_by('show_time')
    hall_name = sessions[0].hall.name

    tickets_num = []
    sale_amount = []

   
    for session in sessions:
        # здесь было бы уместно сравнить количество бкупленных билетов с вместимостью зала
        num = len(Ticket.objects.filter(session=session))
        tickets_num.append(num)
        sale_amount.append(num * session.price)

    
    # в html pop выводит и удаляет последний элемент, поэтому:
    tickets_num.reverse()
    sale_amount.reverse()

    
    context={'sessions': sessions, 'hall_name': hall_name, 'tickets_num': tickets_num, 'sale_amount': sale_amount}

    # return render(request,'cinema\ticket_sessions.html',context=context)
    return render(request,'cinema\\ticket_sessions.html',context=context)


