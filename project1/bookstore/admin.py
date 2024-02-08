from django.contrib import admin
from .models import Book
# Register your models here.
class Bookadmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("title",)}
    list_display=("title","author")
    list_filter=("author","rating")


admin.site.register(Book,Bookadmin)
