from django.shortcuts import render
from .models import MarksAwarded
from result.models import Question, Subject

# Create your views here.
def login(request):
    return render(request, 'base.html')

def register(request):
    return render(request, 'base.html')

def addMarks(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'base.html')

def result(request):
    return render(request, 'base.html')

def subjectSelection(request):
    return render(request, 'base.html')