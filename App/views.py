from django.shortcuts import render

# Create your views here.
from django.views.generic import *
from App.models import *

class SchoolList(ListView):
    model=School
    # template_name='App\school_list.html'
    context_object_name='SLO'
    # queryset=School.objects.get(Scname='ZPHS')
    ordering=['pk']

class StudentList(ListView):
    model=Student
    # template_name='App\school_list.html'
    context_object_name='STO'
    # queryset=School.objects.get(Scname='ZPHS')
    ordering=['pk']

class SchoolDetail(DetailView):
    model=School
    context_object_name='DOSI'

