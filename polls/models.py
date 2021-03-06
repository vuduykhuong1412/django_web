from secrets import choice
from statistics import mode
from unicodedata import name

from django.db import models

# Create your models here.
class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('Date published')
    def __str__(self):
        return self.question_text
class Choice(models.Model):
    question= models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    author = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()
    def __str__(self):
        return self.headline
        
    