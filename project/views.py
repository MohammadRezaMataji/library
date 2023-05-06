from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
Bookslist = [
    {
        'id': '1',
        'title': 'MATH THEORY',
        'description': 'The basic Theory of Math'
    },
    {
        'id': '2',
        'title': 'NEW LIFE',
        'description': 'The view about New born'
    },
    {
        'id': '3',
        'title': 'Social',
        'description': 'About Social Activity'
    }
]

def projects(request):
    Books = Book.objects.all()
    context = {'books':Books}
    return render(request,'project/projects.html', context)

def project(request,pk):
    bookObj = Book.objects.get(id= pk)
    return render(request,'project/project.html',{'book':bookObj})

# Create your views here.
