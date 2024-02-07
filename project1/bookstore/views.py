from django.shortcuts import render
from .models import Book
# Create your views here.
def index(request1):
    books=Book.objects.all()
    return render(request1,"index.html",{"books":books})