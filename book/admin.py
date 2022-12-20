from django.contrib import admin

from .models import Author, Book, Genre, Reward


class AuthorAdmin(admin.ModelAdmin):
    fields = ('first_name','second_name','surname','birthday','deathday','description', 'rewards')


class BookAdmin(admin.ModelAdmin):
    fields = ('title','author', 'genres', 'publish_date')

    def get_genres(self,obj):
        pass

class GenreAdmin(admin.ModelAdmin):
    fields = ('name', 'description',)


class RewardAdimin(admin.ModelAdmin):
    fields = ('name', 'date', 'description')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Reward, RewardAdimin)
