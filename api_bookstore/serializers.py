from django.conf.global_settings import AUTH_USER_MODEL
from rest_framework import serializers

from .models import Book
from .models import Author

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', 'description', 'author_id', 'added_by_id')

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('name', 'added_by_id')


