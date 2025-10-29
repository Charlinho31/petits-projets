from django.shortcuts import render
from datetime import datetime

def index(request): # view function

    return render(request, "DocBlog/index.html", context={"date": datetime.now()}) # retourne le template du site racine DogBlog avec la date actuelle