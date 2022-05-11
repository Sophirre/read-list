from rest_framework import serializers
from read_list_app.models import (
    Book,
    Genre,
    Section,
)


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', 'author', 'genre', 'section', 'is_read')


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('title',)


class SectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Section
        fields = ('title', 'is_complete', 'is_active', 'is_pin', 'creation_date',)
