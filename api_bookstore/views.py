from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import BookSerializer
from .serializers import AuthorSerializer

from .models import Book
from .models import Author

'''
    Viewsets de ambos serializadores para
    realizar el CRUD de ambos modelos de datos.
'''
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('name')
    serializer_class = AuthorSerializer