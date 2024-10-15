from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_view, name = 'index'),
    path('book/', views.ListBookView.as_view(), name = 'list-book'),
    path('book/<int:pk>/detail/', views.DetailBookView.as_view(), name = 'detail-book'),
    path('book/create/', views.CreateBookView.as_view(), name = 'create-book'),
    path('book/<int:pk>/delete/', views.DeleteBookView.as_view(), name = 'delete-book'),
    path('book/<int:pk>/update/', views.UpdateBookView.as_view(), name = 'update-book'),
    path('book/<int:book_id>/review/', views.CreateReviewView.as_view(), name = 'review'),
    path('book/question/', views.CreateQuestionView.as_view(), name = 'question'),
    path('add-to-favorites/<int:book_id>/', views.add_to_favorites, name='add-to-favorites'),
    path('add-to-haveread/<int:book_id>/', views.add_to_havereadbooks, name='add-to-havereadbooks'),
    path('mypage/', views.mypage, name='mypage'),
    path('book/review/<int:review_id>/like', views.add_likes, name = 'add-likes'),
]
