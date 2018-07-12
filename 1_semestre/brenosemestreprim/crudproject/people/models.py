from django.db import models
from django.urls import reverse 

class Person(models.Model): 
    name = models.CharField(max_length=200)
    idade = models.IntegerField()
    cpf = models.CharField(max_length=20)
    email = models.CharField(max_length=200)

    def __str__(self): 
        return self.name
    
    def get_absolute_url(self): 
        return reverse('pessoa_edit', kwargs={'pk': self.pk})
