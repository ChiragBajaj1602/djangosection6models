from django.contrib import admin
from .models import Book,Author
# Register your models here.
class Bookadmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("title",)}
    list_display=("title","author")
    list_filter=("author","rating")

class Author_Admin(admin.ModelAdmin):
    list_display=("lname","fname")
admin.site.register(Book,Bookadmin)
admin.site.register(Author,Author_Admin)
