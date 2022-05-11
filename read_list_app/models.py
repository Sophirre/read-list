from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=70)
    author = models.ForeignKey(
        'Author',
        on_delete=models.SET_NULL,
        related_name='books',
        null=True
    )

    genre = models.ForeignKey(
        'Genre',
        on_delete=models.SET_NULL,
        related_name='books',
        null=True
    )

    section = models.ForeignKey(
        'Section',
        on_delete=models.SET_NULL,
        related_name='books',
        null=True
    )
    is_read = models.BooleanField()


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)


class Section(models.Model):
    title = models.CharField(max_length=70)
    is_complete = models.BooleanField()
    is_active = models.BooleanField()
    is_pin = models.BooleanField()
    creation_date = models.DateField()


class Genre(models.Model):
    title = models.CharField(max_length=25)

