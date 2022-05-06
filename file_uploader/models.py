from dataclasses import field
from pyexpat import model
from statistics import mode
from turtle import title
import django
from django import forms
from django.db import models

from django.forms import ModelForm

from django import forms
# Create your models here.

TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
)
# Cách 2
class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3, choices=TITLE_CHOICES)
    birth_date = models.DateField(blank=True, null=True)

class Book(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'title', 'birth_date']

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'authors']


# Cách 1:

# class AuthorForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     title = forms.CharField(max_length=3, widget=forms.Select(choices=TITLE_CHOICES))
#     birth_date = forms.DateField(required=False)

# class BookForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())