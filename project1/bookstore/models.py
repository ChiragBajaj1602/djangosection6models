from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.
class Country(models.Model):
    name=models.CharField(max_length=50)
    code=models.CharField(max_length=2)
class Address(models.Model):
    street=models.CharField(max_length=100)
    postal_code=models.IntegerField()
    city=models.CharField(max_length=80)
    def __str__(self):
        return f'{self.street} {self.city} {self.postal_code}'
    class Meta:
        verbose_name="Rasta"
        verbose_name_plural="Address Entries"
class Author(models.Model):
    fname=models.CharField(max_length=50,null=True)
    lname=models.CharField(max_length=51,null=True)
    address=models.OneToOneField(Address,on_delete=models.CASCADE,null=True,related_name="author")
    def __str__(self):
        return f'{self.fname} {self.lname} {self.address}'
class Book(models.Model):
    title=models.CharField(max_length=50)
    rating=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    author=models.ForeignKey(Author,on_delete=models.CASCADE,null=True,related_name="malik")
    isbestselling=models.BooleanField(default=False)
    published_countries=models.ManyToManyField(Country,related_name="desh")
    slug=models.SlugField(default="",null=False,blank=True)
    def __str__(self):
        return f"{self.title} {self.author} {self.rating} {self.isbestselling}"
    def get_absolute_url(self):
        return reverse("post-details",args=[self.id])
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super().save(*args,**kwargs)
class Fruit(models.Model):
    name=models.CharField(max_length=100)
class publications(models.Model):
    title=models.CharField(max_length=30)
    class Meta:
        ordering = ["title"]
    def __str__(self):
        return f'{self.title}'
    
class Article(models.Model):
    headline=models.CharField(max_length=100)
    publictaions=models.ManyToManyField(publications,related_name="akhbar")
    def __str__(self):
        return self.headline

