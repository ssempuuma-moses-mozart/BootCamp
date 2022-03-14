from django.db import models
from django.urls import reverse


class Memos(models.Model):
    title = models.CharField(max_length = 250)
    body = models.TextField()
    authorz = models.ForeignKey('auth.user', on_delete = models.CASCADE)
    dat = models.DateField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('details')


        
     
     


