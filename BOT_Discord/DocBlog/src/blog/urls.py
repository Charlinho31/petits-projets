from django.urls import path
from .views import index, article

urlpatterns = [
    path('', index, name="blog-index"), # root URL de l'app blog
    path('article-<str:numero_article>/', article, name="blog-article"), # URL pour les articles, avec un paramètre dynamique 'numero_article'
]