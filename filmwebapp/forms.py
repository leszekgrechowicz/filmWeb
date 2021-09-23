from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from filmwebapp.models import Genre, Person
from datetime import datetime

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
    rating = forms.DecimalField(max_digits=2, decimal_places=1)
    genre = forms.ChoiceField(choices=Genre.GENRE_CHOICES)



    def clean_rating(self, *args, **kwargs):
        rating = self.cleaned_data.get("rating")
        if 1.0 > rating > 10.0:
            raise forms.ValidationError("Rating should be between 1.0 and 10.0")
        return rating

    def clean_production_year(self):
        production_year = self.cleaned_data.get('production_year')
        todays_date = datetime.now()
        if production_year < 1700 or production_year > todays_date.year:
            raise forms.ValidationError("Please provide correct production year")
        return production_year



