from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('list/',views.list,name='list'),
    path('interest/<int:service_id>',views.interest,name='interest')
]
