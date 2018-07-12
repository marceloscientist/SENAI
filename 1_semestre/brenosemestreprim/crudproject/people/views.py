#from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy 

from people.models import Person 

class PersonList(ListView): 
    model = Person

class PersonView(DetailView): 
    model = Person

class PersonCreate(CreateView): 
    model = Person
    fields = ['name','idade','cpf','email']
    success_url = reverse_lazy('person_list')

class PersonUpdate(UpdateView): 
    model = Person
    fields = ['name','idade','cpf','email']
    success_url = reverse_lazy('person_list')

class PersonDelete(DeleteView): 
    model = Person
    success_url = reverse_lazy('person_list')
