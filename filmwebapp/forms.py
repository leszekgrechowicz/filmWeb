from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from filmwebapp.models import Genre, Person

class EditForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()


class MovieForm(forms.Form):
    MIN = 1.0
    MAX = 10.0
    title = forms.CharField()
    director = forms.ModelChoiceField(queryset=Person.objects.all())
    screenplay = forms.ModelChoiceField(queryset=Person.objects.all())
    starring = forms.ModelChoiceField(queryset=Person.objects.all())
    starring2 = forms.ModelChoiceField(queryset=Person.objects.all())
    # starring3 = forms.ModelChoiceField(queryset=Person.objects.all())

    production_year = forms.IntegerField()
    rating = forms.DecimalField(max_digits=2, decimal_places=1,
                                validators=[MinValueValidator(MIN), MaxValueValidator(MAX)])
    genre = forms.ChoiceField(choices=Genre.GENRE_CHOICES)

    # genre1 = forms.ChoiceField(choices=Genre.GENRE_CHOICES)
    # genre3 = forms.ChoiceField(choices=Genre.GENRE_CHOICES)



