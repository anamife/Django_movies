from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView
from django.db.models import Q

from .models import Movie, Category, Actor, Genre
from .forms import ReviewForm


class GenreYear:
	def get_genres(self):
		return Genre.objects.all()

	def get_years(self):
		return Movie.objects.filter(draft=False).values('year')


# class MoviesView(View):
# 	def get(self, request):
# 		movies = Movie.objects.all()
# 		return render(request, "movies/movies.html", {"movie_list": movies})


#class MovieDetailView(View):
# 	def get(self, request, slug):
# 		movie = Movie.objects.get(url=slug)
# 		return render(request, 'movies/movie_detail.html', {'movie': movie})
		
class MoviesView(GenreYear, ListView):
	model = Movie
	queryset = Movie.objects.filter(draft=False) # Создается объект movie_list
	template_name = 'movies/movie_list.html'


	# Поскольку функция get_context_data есть в нескольких Views
	# def get_context_data(self, *args, **kwargs):
	# 	context = super().get_context_data(*args, **kwargs)
	# 	context['categories'] = Category.objects.all()
	# 	return context


class MovieDetailView(GenreYear, DetailView):
	model = Movie
	slug_field = "url"


	# Мы здесь не указываем template_name, потому что django автоматически подставляет 'названиемодели_detail.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['star_form'] = RatingForm()
		return context


class AddReview(View):
	def post(self, request, pk):
		form = ReviewForm(request.POST)
		movie = Movie.objects.get(id=pk)
		if form.is_valid():
			form = form.save(commit=False)
			if request.POST.get("parent", None):
				form.parent_id = int(request.POST.get('parent'))
			form.movie = movie
			form.save()
		return redirect(movie.get_absolute_url())


class ActorView(GenreYear, DetailView):
	model = Actor
	template_name = 'movies/actor.html'
	slug_field = 'name'


class FilterMoviesView(GenreYear, ListView):
	def get_queryset(self):
		queryset = Movie.objects.filter(
			Q(year__in=self.request.GET.getlist('year')) |
			Q(genres__in=self.request.GET.getlist('genres'))
			)
		return queryset










