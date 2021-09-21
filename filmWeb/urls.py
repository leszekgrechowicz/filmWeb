"""filmWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from filmwebapp.views import show_movies, movie_details, show_persons, \
    EditPersonView, AddPersonView, AddMovieView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', show_movies, name='movies'),
    path('movie-details/<int:pk>', movie_details, name='movie'),
    path('persons/', show_persons, name='persons'),
    path('edit-person/<int:pk>', EditPersonView.as_view(), name='edit-person'),
    path('add-person/', AddPersonView.as_view(), name='add-person'),
    path('add-movie/', AddMovieView.as_view(), name='add-movie'),

]
