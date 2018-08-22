from django.shortcuts import render
from .models import Post

def index(request):
	lastRecipes = Post.objects.order_by('-datePosted')
	return render(request, 'recipeblog/index.html', {'lastRecipes': lastRecipes})

#def recipe(request, recipe):
