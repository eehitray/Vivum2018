from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

import datetime

def index(request):
	lastRecipes = Post.objects.order_by('-datePosted')
	return render(request, 'recipeblog/index.html', {'lastRecipes': lastRecipes})

def submit(request):
	if request.POST:
		try:
			username = request.POST['username']
			recipename = request.POST['recipename']
			ingredients = request.POST['ingredients']
			url = request.POST['url']
			instructions = request.POST['instructions']
		except:
			return render(request, 'recipeblog/form.html', {error: 'You have left one or more fields blank.'})
		else:
			p = Post(
					title=recipename,
					ingredients='',
					contents=instructions,
					picture=url,
					datePosted=datetime.date.today()
				)
			ingredients = "'" + ingredients + "'"
			p.setIngredients(ingredientsText = ingredients)
			p.save()
			return HttpResponse('that worked yo')
	else: 
		return HttpResponse('404 nigga')

