from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.sessions,name = 'sessions'),
    path('index/',views.index,name='index'),
    path('in_hall/<int:hall_id>',views.sessions_in_hall,name='in_hall'),
    path('by/<int:session_id>',views.by_ticket,name='by_ticket'),
    path('sold/',views.tickets_sold,name='tickets_sold'),
    path('add_movie/', views.add_movie, name='add_movie'),
    path('add_session/',views.add_session,name='add_session'),
    path('movie/<int:movie_id>',views.movie,name='movie'),
    path('edit_movie/<int:id_movie>',views.edit_movie,name='edit_movie'),
    path('edit_session/<int:id_session>',views.edit_session,name='edit_session')
    
]
