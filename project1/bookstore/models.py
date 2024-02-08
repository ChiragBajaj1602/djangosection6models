from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.
class Author(models.Model):
    fname=models.CharField(max_length=50,null=True)
    lname=models.CharField(max_length=51,null=True)
    def __str__(self):
        return f'{self.fname} {self.lname}'
class Book(models.Model):
    title=models.CharField(max_length=50)
    rating=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    author=models.ForeignKey(Author,on_delete=models.CASCADE,null=True,related_name="malik")
    isbestselling=models.BooleanField(default=False)
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

