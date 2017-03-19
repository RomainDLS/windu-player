from django.contrib import admin

# Register your models here.
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    model = Movie

    list_display = ['title', 'duration']

admin.site.register(Movie, MovieAdmin)
