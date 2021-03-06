from turtle import update
from venv import create
from django.contrib.auth.models import User 
from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True) #para as urls seen unicas
    author = models.ForeignKey(User, on_delete=models.CASCADE) ## Para que o usuario seja unico e 
    boby = models.TextField() # são os post do blog
    create = models.DateTimeField(auto_now_add=True) # vai guarda data e hora automatico
    updated = models.DateTimeField(auto_now=True) # vai salva as modifições 

    class Meta:
        ordering = ("-create",) # ordena os post em oreder que foi criado

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})
    


