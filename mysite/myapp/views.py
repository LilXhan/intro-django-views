from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Person
from .forms import PersonForm
from django.views.generic import View, TemplateView, CreateView, FormView
from django.core import serializers

import json

# Vistas o Views (Controladores)

# Function-Based Views (basados en funciones)

# siempre las funciones reciben un request
def index(request):
    return HttpResponse('Hello World, from Django')


def index_two(request):
    if request.method == 'GET':
        print('GET')
    elif request.method == 'POST':
        print('POST')
        return HttpResponse('Index')
    
    return HttpResponse('Index')


def index_three(request):
    people = Person.objects.all()

    context = {
        'people': people
    }

    if request.method == 'POST':
        # La logica para crear una nueva person
        person = Person.objects.create(name=request.POST['name'])

    return render(request, 'index.html', context)

# Class-Based Views (basados en clases)

class IndexView(View):
    # tiene los metodos predefinidos
    def get(self, request):
        # print(request.session.get('people_name'))
        # request.session['people_name'] = people[0].name

        # Recomendado para data que no cambia o cambia rara vez 
        # -> como paises, ciudades, codigos de pais, etc

        people = []

        if request.session.get('people'):
            people_session = json.loads(request.session.get('people'))

            for person in people_session:
                people.append(person['fields'])

        if len(people) == 0:
            people = Person.objects.all()        
            # Convertir de query set a json para guardarlo en una cockie o cache
            request.session['people'] = serializers.serialize('json', people) 
    
        context = {
            'people': people 
        }

        return render(request, 'index.html', context)

    def post(self, request):
        # logica para crear una persona 
        person = Person.objects.create(name=request.POST['name'])

        return redirect('index')


class IndexTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        people = []

        if self.request.session.get('people'):
            people_session = json.loads(self.request.session.get('people'))
            for person in people_session:
                people.append(person['fields'])

        if len(people) == 0:
            people_query = Person.objects.all()
            self.request.session['people'] = serializers.serialize('json', people_query)

        print(people)

        context['people'] = people
        return context


# Formulario Class View

class IndexCreateView(CreateView):
    template_name = 'index.html'
    fields = ['name', 'email', 'address']
    model = Person
    success_url = '/myapp'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['people'] = Person.objects.all()
        return context


class CreatePerson(View):

    def get(self, request):
        form = PersonForm()

        context = {
            'form': form
        }

        return render(request, 'form.html', context)

    def post(self, request):
        # vamos a poder acceder a la informacion enviada por el formulario de html
        form = PersonForm(request.POST)
        
        if form.is_valid():
            # accediendo a el input de los inputs
            cleaned_data = form.cleaned_data
            person = Person.objects.create(**cleaned_data)
            person.save()

            return redirect('index')


class PersonCreateForm(FormView):
    template_name = 'form.html'
    form_class = PersonForm

    # para guardar la informacion existe una función que se encarga de verificar si el formulario
    # es valido -> def form_valid()

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        person = Person.objects.create(**cleaned_data)
        person.save()
        return redirect('index')

    def form_invalid(self, form):
        print('erros ->', form.errors)
        return redirect('index')