from rest_framework import serializers
from news.models import *
from datetime import datetime

    
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            'id',
            'type',
            'by',
            'title',
            'text',
            'url',
            'time',
            'descendants',
            'score',
            'parents',
        ]
    def create(self, validated_data):
        return Item.objects.get_or_create(**validated_data)
    
            
class CommentsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    by = serializers.CharField(max_length=30)
    text = serializers.CharField()
    time = serializers.IntegerField()
    parent = serializers.PrimaryKeyRelatedField(source='item.id', queryset=Item.objects.all())
    class Meta:
        model = Comment
        fields = [
            'id',
            'by', 
            'text',
            'time',
            'parent'
        ]
    def create(self, validated_data):
        par = validated_data.pop("item")
        parent = par.pop('id')
        print(parent.id)
        try:
            item = Item.objects.get(id = int(parent.id))
        except Item.DoesNotExist:
            return None
        return Comment.objects.get_or_create( parent=parent,**validated_data)
    
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'by', 
            'text',
            'parent'
        ]
    def create(self, validated_data):
        parent = validated_data.pop("parent")
        return Comment.objects.create( parent=parent, **validated_data)
    
class ItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            'id',
            'by', 
            'title',
            'url',
            'text',
            'type',
            'score'
        ]
    def create(self, validated_data):
        return Item.objects.create(created_with_api=True, **validated_data)
    
class ItemsSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Item
        fields = [
            'id',
            'by',
            'type',
            'title',
            'comments',
            'url',
            'deleted',
            'dead',
            'score'
        ]