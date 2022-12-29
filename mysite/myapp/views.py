from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

# siempre las funciones reciben un request
def index(request):
    return HttpResponse('Hello World, from Django')


def index_two(request):
    people = Person.objects.all()

    context = {
        'people': people
    }

    return render(request, 'index.html', context)