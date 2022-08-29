from django.urls import path
from .views import *


urlpatterns = [
    path('', ItemCreate.as_view()),
    path('comments/', CommentsCreate.as_view()),
    path('news/', ItemList.as_view()),
    path('new/story/', ItemCreateAPI.as_view()),
    path('new/comment/', CommentCreateAPI.as_view()),
    path('news/<int:id>/', UpdateDestroyView.as_view())
]