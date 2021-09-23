from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    MIN = -1
    MAX = 8
    GENRE_CHOICES = (
        (0, 'Not defined'),
        (1, 'Action'),
        (2, 'Thriller'),
        (3, 'Science Fiction'),
        (4, 'Fantasy'),
        (5, 'Comedy'),
        (6, 'Romantic'),
        (7, 'Western'),
        (8, 'Crime'),
        (9, 'Drama')
    )
    name = models.IntegerField(choices=GENRE_CHOICES, default=-1,
                               validators=[MinValueValidator(MIN), MaxValueValidator(MAX)])

    def __str__(self):
        return f"{self.name}"


class Movie(models.Model):
    MIN = 1.0
    MAX = 10.0
    title = models.CharField(max_length=128, unique=True)
    director = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="director+")
    screenplay = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="screenplay+")
    starring = models.ManyToManyField(Person, through="PersonMovie")
    year = models.IntegerField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    # validators=[MinValueValidator(MIN), MaxValueValidator(MAX)])
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return f"{self.title}"


class PersonMovie(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    role = models.CharField(max_length=128)



