from django.views.generic import ListView, UpdateView, DeleteView,DetailView
from django.urls import reverse_lazy
from .models import Memos

class MemoHomeView(ListView):
    model = Memos
    template_name = 'index.html'
    context_object_name = 'memo'

class MemoDetailView(ListView):
    model = Memos
    template_name = 'details.html'
    context_object_name = 'memo'    

class MemoUpdateView(UpdateView):
    model =  Memos
    template_name = 'update.html'  
    fields   = ['title','body']  

class MemoDeleteView(DeleteView):
    model =  Memos
    template_name = 'delete.html'  
    success_url = reverse_lazy('index')        

