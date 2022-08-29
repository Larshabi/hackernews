from django.shortcuts import render, Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Item, Comment
from django.db.models import Q
from datetime import datetime

def search(request):
    queryset = Item.objects.all()
    query = request.GET.get("search")
    if query:
        queryset= queryset.filter(
            Q(title__icontains=query)|
            Q(by__icontains=query)|
            Q(type__icontains=query)|
            Q(comments__text__icontains=query)|
            Q(comments__by__icontains=query)|
            Q(text__icontains=query)
            ).distinct()
    context = {'items':queryset}
    return render(request, 'news/home.html', context)
    
def filter(request, type):
    queryset = Item.objects.all()
    query = type
    if query:
        queryset = queryset.filter(
             Q(type__icontains=query)|
             Q(comments__type__icontains=query)
        ).distinct()
    return render(request, 'news/home.html', {'items':queryset})

class Filter(ListView):
    template_name = 'news/home.html'
    paginate_by = 10
    context_object_name= 'items'
    def get_queryset(self):
        self.query = self.kwargs["type"]
        if self.query:
            queryset = Item.objects.all().filter(
             Q(type__icontains=self.query)|
             Q(comments__type__icontains=self.query)
        ).order_by('-time').distinct()
        return queryset
    
    
    
class ItemList(ListView):   
    model = Item
    paginate_by = 10
    template_name='news/home.html'
    context_object_name='items'
    ordering = '-time'
    def get_queryset(self):
        return Item.objects.all().order_by('-time')
   
class ItemDetail(DetailView):
    model = Item
    template_name = 'news/detail.html'
    context_object_name = 'item'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["commented"] = Comment.objects.filter(parent=context["object"].id)
        context["new_time"] = datetime.fromtimestamp(context["object"].time)
        return context
        