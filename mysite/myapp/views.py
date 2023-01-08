from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Person
from django.views.generic import View, TemplateView, CreateView


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
        people = Person.objects.all()

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
    extra_context = {
        'people': Person.objects.all()
    }

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['people'] = Person.objects.all()
    #     return context


# Formulario Class View

class IndexCreateView(CreateView):
    template_name = 'index.html'
    fields = ['name', 'email', 'address']
    model = Person

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['people'] = Person.objects.all()
        return context
