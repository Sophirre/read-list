from rest_framework.decorators import api_view
from rest_framework.response import Response
from read_list_app.models import (
    Book,
    Section,
    Author,
    Genre
)


@api_view(["GET", "POST"])
def api_books(req):
    pass


@api_view(["GET", "POST"])
def api_sections(req):
    pass

