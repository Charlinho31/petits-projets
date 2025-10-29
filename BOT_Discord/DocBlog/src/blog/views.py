from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'blog/index.html' , context={"date": datetime.now()}) # retourne le template index.html de l'application blog avec la date actuelle

def article(request, numero_article):
    if numero_article in ['01', '02', '03']: # vérifie si le numéro de l'article est valide
        return render(request, f"blog/article_{numero_article}.html") # retourne le template correspondant à l'article
    return render(request, "blog/article_not_found.html") # retourne un template d'erreur si l'article n'existe pas