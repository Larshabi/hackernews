from re import T
from django.db import models


class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=100)
    by = models.CharField(max_length=50)
    time = models.IntegerField(null=True, blank=True)
    deleted = models.BooleanField(default=False)
    dead =models.BooleanField(default=False)
    text = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    descendants = models.IntegerField(null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    parents = models.IntegerField(null=True, blank=True)
    created_with_api = models.BooleanField(default=False)
    
    def __str__(self):
        if self.title:
            return self.title
        return f'{self.id}'

class Parts(models.Model):
    id = models.IntegerField(primary_key=True)
    polls = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='parts', null=True, blank=True)
    
    
class Comment(models.Model):
    by = models.CharField(max_length=30)
    id = models.IntegerField(primary_key=True)
    text = models.TextField(null=True, blank=True)
    deleted = models.BooleanField(default=False)
    time = models.IntegerField(null=True, blank=True)
    parent = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='comments')
    type = models.CharField(max_length=10, default='comment')
    def __str__(self):
        return self.by
    