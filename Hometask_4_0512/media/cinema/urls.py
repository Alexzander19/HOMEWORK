from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.sessions,name = 'sessions'),
    path('index/',views.index,name='index'),
    path('in_hall/<int:hall_id>',views.sessions_in_hall,name='in_hall'),
    path('by/<int:session_id>',views.by_ticket,name='by_ticket'),
    path('sold/',views.tickets_sold,name='tickets_sold')
    
]
