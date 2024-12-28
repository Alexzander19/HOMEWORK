from django.shortcuts import redirect, render

from .forms import MovieAddForm, SessionAddForm
from .models import Movie, Session, Ticket

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
        
        num = len(Ticket.objects.filter(session=session))
        tickets_num.append(num)
        sale_amount.append(num * session.price)

    
    # в html pop выводит и удаляет последний элемент, поэтому:
    tickets_num.reverse()
    sale_amount.reverse()

    
    context={'sessions': sessions, 'hall_name': hall_name, 'tickets_num': tickets_num, 'sale_amount': sale_amount}

    # return render(request,'cinema\ticket_sessions.html',context=context)
    return render(request,'cinema\\ticket_sessions.html',context=context)


def add_movie(request):
    if request.method == "POST":
        form = MovieAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie',movie.id)
    else:
        form = MovieAddForm()
  
    return render(request, 'cinema/add_movie.html', context={'form': form})

def edit_movie(request,id_movie):
    movie = Movie.objects.get(id=id_movie)
    if request.method == "POST":
        form = MovieAddForm(instance=movie, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie', movie_id=id_movie)
    else:
        form = MovieAddForm(instance=movie)
    context={'form': form, 'movie': movie}
    return render(request, 'cinema/edit_movie.html', context=context)


def add_session(request):
    if request.method == "POST":
        form = SessionAddForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SessionAddForm()

    return render(request, "cinema/add_session.html", {"form": form})

def edit_session(request,id_session):
    session = Session.objects.get(id=id_session)
    if request.method == "POST":
        form = SessionAddForm(instance=session, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('tickets_sold')
    else:
        form = SessionAddForm(instance=session)
    context={'form': form, 'session': session}
    return render(request, 'cinema/edit_session.html', context=context)


def movie(request,movie_id):
    movie = Movie.objects.get(id=movie_id)
    sessions = Session.objects.filter(movie=movie).order_by('show_time')
    
    context={'sessions': sessions, 'movie': movie}

    return render(request,'cinema\movie.html',context=context)
