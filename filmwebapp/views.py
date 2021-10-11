from django.shortcuts import render
from filmwebapp.models import Movie, Person, Genre
from django.views.generic import TemplateView, FormView
from filmwebapp.forms import EditForm, MovieForm, EditMovieForm
from django.contrib import messages
from django.shortcuts import redirect


def show_movies(request):
    """Queries all movies"""
    title = "Movies"
    movies = Movie.objects.all().order_by('-year')
    link = True
    if not movies:
        messages.info(request, 'Database is empty, please create some movies.')

    return render(request, 'movies.html', {'link': link, 'title': title, 'movies': movies})


def movie_details(request, pk):
    """Queries movie details"""
    title = "Movie Details"
    movie = Movie.objects.get(id=pk)

    return render(request, 'movies.html', {'title': title, 'movies': [movie, ]})


def show_persons(request):
    title = "Persons"
    persons = Person.objects.all()
    if not persons:
        messages.info(request, 'Database is empty, please create some persons.')
    return render(request, 'persons.html', {'title': title, 'persons': persons})


class EditPersonView(FormView):
    """Edits person details"""
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
            messages.success(request, 'Person details updated.')
            return redirect(show_persons)


class AddPersonView(FormView):
    """Adds person to the database"""
    template_name = 'addperson.html'
    title = 'Add Person'

    def get(self, request):
        form = EditForm()
        return render(request, self.template_name, {'form': form, 'title': self.title})

    def post(self, request):
        form = EditForm(request.POST or None)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            person_to_add = Person.objects.create(first_name=first_name, last_name=last_name)
            messages.success(request, f'Person {person_to_add.first_name} has been added to the database.')
            return redirect(show_persons)


class AddMovieView(TemplateView):
    """Adds """

    template_name = 'addmovie.html'
    title = 'Add Movie'

    def get(self, request):
        form = MovieForm()
        args = {'title': self.title, 'form': form}
        return render(request, self.template_name, args)

    def post(self, request):
        form = MovieForm(request.POST or None)
        if form.is_valid():
            new_movie = Movie.objects.create(title=form.cleaned_data['title'],
                                             director=form.cleaned_data['director'],
                                             screenplay=form.cleaned_data['screenplay'],
                                             year=form.cleaned_data['production_year'],
                                             rating=form.cleaned_data['rating'])

            new_movie.starring.set([form.cleaned_data['starring'], form.cleaned_data['starring2']])
            new_movie.genres.set([Genre.objects.get(name=int(form.cleaned_data['genre'])), ])
            return redirect(show_movies)

        else:
            return render(request, 'addmovie.html', {'title': self.title, 'form': form})


class EditMovieView(FormView):
    template_name = 'editmovie.html'
    title = 'Edit Movie'

    def get(self, request, pk):
        movie = Movie.objects.get(id=pk)
        stars = movie.starring.all()
        genre = movie.genres.all()

        stars1, stars2 = None, None

        if stars:
            stars1 = stars[0]
        if len(stars) > 1:
            stars2 = stars[1]

        pre_data = {'title': movie.title,
                    'director': movie.director,
                    'screenplay': movie.screenplay,
                    'starring': stars1,
                    'starring2': stars2,
                    'production_year': movie.year,
                    'rating': movie.rating,
                    'genre': genre[0],
                    'hidden': 0,
                    }
        form = EditMovieForm(initial=pre_data)
        context = {'title': self.title, 'form': form}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        form = EditMovieForm(request.POST or None)
        if form.is_valid():
            Movie.objects.filter(id=pk).update(title=form.cleaned_data['title'],
                                               director=form.cleaned_data['director'],
                                               screenplay=form.cleaned_data['screenplay'],
                                               year=form.cleaned_data['production_year'],
                                               rating=form.cleaned_data['rating'])

            movie_to_edit = Movie.objects.get(id=pk)
            movie_to_edit.starring.set([form.cleaned_data['starring'], form.cleaned_data['starring2']])
            movie_to_edit.genres.set([form.cleaned_data['genre'], ])
            return redirect(show_movies)

        else:
            return render(request, self.template_name, {'title': self.title, 'form': form})


class DeletePerson(TemplateView):

    def get(self, request, pk):
        object_to_delete = Person.objects.get(id=pk)
        object_to_delete.delete()
        messages.success(request,
                         f'Person {object_to_delete.first_name} {object_to_delete.last_name} has been deleted.')
        return redirect(show_persons)


class DeleteMovie(TemplateView):

    def get(self, request, pk):
        object_to_delete = Movie.objects.get(id=pk)
        object_to_delete.delete()
        messages.success(request, f'Movie {object_to_delete.title} has been deleted.')
        return redirect(show_movies)
