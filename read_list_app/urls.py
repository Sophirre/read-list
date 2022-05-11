from django.urls import path

from read_list_app.views import (
    api_books,
    api_sections,
)
urlpatterns = [
    path('books/', api_books),
    path('sections/', api_sections)

]
