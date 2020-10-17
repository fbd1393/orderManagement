from django.shortcuts import render
from django.http import HttpResponse

users = [
    {
        'name': 'adam',
        'id': '1',
        'age': '19'
    },
    {
        'name': 'barbara',
        'id': '2',
        'age': '17'
    },
    {
        'name': 'mandy',
        'id': '3',
        'age': '17'
    },
]


def home(request):
    context = {
        'users': users,
        'title': 'Home'
    }
    return render(request, 'ordermanagers/home.html', context)


def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'ordermanagers/about.html', context)
