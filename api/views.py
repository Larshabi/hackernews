from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializer import *
from .permission import UpdateOrDelete

class ItemCreate(GenericAPIView):
    serializer_class = ItemSerializer
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Done'}, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CommentsCreate(GenericAPIView):
    serializer_class = CommentsSerializer
    permission_classes = [AllowAny] 
    def post(self, request):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Done'}, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemList(ListAPIView):
    serializer_class = ItemsSerializer
    permission_classes = [AllowAny]
    queryset = Item.objects.all()
    filterset_fields = [
        'type'
    ]
    search_fields= [
        'comments__text',
        'type',
        'title',
        'by',
    ]
    
    
class ItemCreateAPI(CreateAPIView):
    serializer_class = ItemCreateSerializer
    permission_classes = [AllowAny]
    queryset = Item.objects.all()
    
class CommentCreateAPI(CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]
    queryset = Comment.objects.all()
    
class UpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = ItemCreateSerializer
    permission_classes = [UpdateOrDelete]
    queryset = Item.objects.all()
    lookup_field = 'id'
