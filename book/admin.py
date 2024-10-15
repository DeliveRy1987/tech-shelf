from django.contrib import admin
# from .models import SampleModel

# admin.site.register(SampleModel)

from .models import Book, Review, Question, FavoriteBook

admin.site.register(Book)
admin.site.register(Review)

admin.site.register(Question)

admin.site.register(FavoriteBook)