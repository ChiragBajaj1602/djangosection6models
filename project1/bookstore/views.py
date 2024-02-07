from django.shortcuts import render
from .models import Book
from django.db.models import Avg
# Create your views here.
def index(request):
    books=Book.objects.all().order_by("rating")
    return render(request,"index.html",{"books":books,
                                        "averagerating":books.aggregate(Avg("rating"))
                                        })
def postdetails(request,id):
    book=Book.objects.get(pk=id)
    return render(request,"book-detail.html",{
        "id":id,
        "title":book.title,
        "author":book.author,
        "rating":book.rating,
        "isbestseller":book.isbestselling,
        "slugify":book.slug
    })