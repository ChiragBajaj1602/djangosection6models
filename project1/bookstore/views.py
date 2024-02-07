from django.shortcuts import render
from .models import Book
# Create your views here.
def index(request):
    books=Book.objects.all()
    return render(request,"index.html",{"books":books})
def postdetails(request,id):
    book=Book.objects.get(pk=id)
    return render(request,"book-detail.html",{
        "title":book.title,
        "author":book.author,
        "rating":book.rating,
        "isbestseller":book.isbestselling
    })