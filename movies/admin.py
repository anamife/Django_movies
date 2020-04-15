from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Genre, Actor, Movie, MovieShots, Rating, RatingStar, Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'url')
	list_display_links = ('name',)

class ReviewInLine(admin.StackedInline):
	model = Review
	extra = 1

class MovieShotsInLine(admin.TabularInline):
	model = MovieShots
	extra = 1
	readonly_fields = ('get_image',)

	def get_image(self, obj):
		return mark_safe(f'<img src={obj.image.url} width="100" height="80" ')

	get_image.short_description = 'Изображение'
	

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url', 'draft')
	list_filter = ('category','year')
	search_fields = ('title', 'category__name')
	inlines = [ReviewInLine, MovieShotsInLine]
	save_on_top = True # Ставим меню с сохранением вверх
	save_as = True # Сохранить как новый объект
	list_editable = ('draft',)  # Можем редактировать прямо в списке
	# fields = (('actors', 'directors', 'genres'),) # Группируем в одну строку


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'parent', 'movie', 'id')
	readonly_fields = ('name', 'email')


	
@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
	list_display = ('name', 'age', 'get_image')
	readonly_fields = ('get_image',)

	def get_image(self, obj):
		return mark_safe(f'<img src={obj.image.url} width="50" height="60" ')

	get_image.short_description = 'Изображение'


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
	list_display = ('title', 'movie', 'get_image')
	readonly_fields = ('get_image',)

	def get_image(self, obj):
		return mark_safe(f'<img src={obj.image.url} width="60" height="50" ')

	get_image.short_description = 'Изображение'
	


#admin.site.register(Category, CategoryAdmin)
#admin.site.register(Actor)
#admin.site.register(Movie)
#admin.site.register(MovieShots)
admin.site.register(Rating)
admin.site.register(Genre)
admin.site.register(RatingStar)
#admin.site.register(Review)


admin.site.site_title = 'Django Movies'
admin.site.site_header = 'Django Movies'




