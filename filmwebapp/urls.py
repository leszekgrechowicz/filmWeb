from django.urls import path
from . import views


urlpatterns = [

    path('', views.show_movies, name='movies'),
    path('movie-details/<int:pk>', views.movie_details, name='movie'),
    path('persons/', views.show_persons, name='persons'),
    path('edit-person/<int:pk>', views.EditPersonView.as_view(), name='edit-person'),
    path('add-person/', views.AddPersonView.as_view(), name='add-person'),
    path('add-movie/', views.AddMovieView.as_view(), name='add-movie'),
    path('edit-movie/<int:pk>', views.EditMovieView.as_view(), name='edit-movie'),

]