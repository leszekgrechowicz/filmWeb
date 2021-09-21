from django.shortcuts import render
from django.http import HttpResponse
from filmwebapp.models import Movie, Person, Genre
from django.views.generic import TemplateView
from filmwebapp.forms import EditForm, MovieForm
from django.contrib import messages
from django.shortcuts import redirect


# Create your views here.


def show_movies(request):
    """Queries all movies"""
    title = "Movies"
    movies = Movie.objects.all().order_by('-year')
    link = True
    return render(request, 'movies.html', {'link': link, 'title': title, 'movies': movies})


def movie_details(request, pk):
    """Queries movie details"""
    title = "Movie Details"
    movie = Movie.objects.get(id=pk)
    movie.starring.all()
    movie.genres.all()
    return render(request, 'movies.html', {'title': title, 'movies': [movie, ]})


def show_persons(request):
    title = "Persons"
    persons = Person.objects.all()
    return render(request, 'persons.html', {'title': title, 'persons': persons})


class EditPersonView(TemplateView):
    template_name = 'editperson.html'
    title = 'Edit Person'

    def get(self, request, pk):
        person_to_edit = Person.objects.get(id=pk)
        form = EditForm()
        args = {'title': self.title, 'person': person_to_edit, 'form': form}
        return render(request, self.template_name, args)

    def post(self, request, pk):
        form = EditForm(request.POST)
        if form.is_valid():
            person_to_edit = Person.objects.get(id=pk)
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            person_to_edit.first_name = first_name
            person_to_edit.last_name = last_name
            person_to_edit.save()
            # messages.success(request, 'Persons details updated.')
            return redirect(show_persons)


class AddPersonView(TemplateView):
    template_name = 'addperson.html'
    title = 'Add Person'

    def get(self, request):
        form = EditForm()
        return render(request, self.template_name, {'form': form, 'title': self.title})

    def post(self, request):
        form = EditForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            person_to_add = Person.objects.create(first_name=first_name, last_name=last_name)
            return redirect(show_persons)


class AddMovieView(TemplateView):
    template_name = 'editmovie.html'
    title = 'Add Movie'

    def get(self, request):
        form = MovieForm()
        args = {'title': self.title, 'form': form}
        return render(request, self.template_name, args)

    def post(self, request):
        form = EditForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            director = form.cleaned_data['director']
            screenplay = form.cleaned_data['screenplay']
            starring = form.cleaned_data['staring']
            year = form.cleaned_data['production_year']
            rating = form.cleaned_data['form']
            genre = form.cleaned_data['genre']
            print(title, screenplay, starring)

            Movie.objects.create(title=title, director=director, screenplay=screenplay, starring=starring,
                                 year=year, rating=rating, genre=genre)

            return redirect(show_movies)
