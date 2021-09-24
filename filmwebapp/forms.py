from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from filmwebapp.models import Genre, Person
from datetime import datetime


class EditForm(forms.Form):
    ATTRS = {
        'class': 'form-control mt-1',

    }

    first_name = forms.CharField(widget=forms.TextInput(
        attrs=ATTRS))

    last_name = forms.CharField(widget=forms.TextInput(
        attrs=ATTRS))


class MovieForm(forms.Form):
    ATTRS = {
        'class': 'form-control mt-1',

    }
    todays_date = datetime.now()

    title = forms.CharField(widget=forms.TextInput(
        attrs=ATTRS))

    director = forms.ModelChoiceField(queryset=Person.objects.all(), widget=forms.Select(
        attrs=ATTRS))

    screenplay = forms.ModelChoiceField(queryset=Person.objects.all(), widget=forms.Select(
        attrs=ATTRS))

    starring = forms.ModelChoiceField(queryset=Person.objects.all(), widget=forms.Select(
        attrs=ATTRS))

    starring2 = forms.ModelChoiceField(queryset=Person.objects.all(), widget=forms.Select(
        attrs=ATTRS))

    # starring3 = forms.ModelChoiceField(queryset=Person.objects.all())

    production_year = forms.IntegerField(min_value=1600, max_value=todays_date.year, widget=forms.NumberInput(
        attrs=ATTRS))

    rating = forms.DecimalField(max_digits=2, decimal_places=1, min_value=1.0, max_value=10.0, widget=forms.NumberInput(
        attrs=ATTRS))

    genre = forms.ChoiceField(choices=Genre.GENRE_CHOICES, widget=forms.Select(
        attrs=ATTRS))

    # def clean_rating(self, *args, **kwargs):
    #     rating = self.cleaned_data.get("rating")
    #     if 1.0 > rating > 10.0:
    #         raise forms.ValidationError("Rating should be between 1.0 and 10.0")
    #     return rating
    #
    # def clean_production_year(self):
    #     production_year = self.cleaned_data.get('production_year')
    #     todays_date = datetime.now()
    #     if production_year < 1700 or production_year > todays_date.year:
    #         raise forms.ValidationError("Please provide correct production year")
    #     return production_year
