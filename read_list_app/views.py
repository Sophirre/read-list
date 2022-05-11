from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from read_list_app.models import (
    Book,
    Section,
    Author,
    Genre,
)

from read_list_app.serializers import (
    BookSerializer,
    SectionSerializer,
    GenreSerializer,
)


@api_view(["GET", "POST"])
def api_books(req):
    if req.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    elif req.method == 'POST':
        serializer = BookSerializer(data=req.data, many=True)
        if serializer.is_valid():
            print("OK")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
def api_sections(req):
    pass

