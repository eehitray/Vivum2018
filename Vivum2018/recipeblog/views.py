from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

import datetime

def index(request):
	lastRecipes = Post.objects.order_by('-datePosted')
	return render(request, 'recipeblog/index.html', {'lastRecipes': lastRecipes, 'text': 'All Recipes'})

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
					postedBy=username,
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

def blog(request, rname):
	try:
		q = Post.objects.get(title = rname)
	except:
		return HttpResponse('404 nigga')
	else:
		title = q.title
		postedBy = q.postedBy
		ingredients = q.getIngredientsList().split(', ')
		ingredients[0] = ingredients[0][1:]
		ingredients[len(ingredients) - 1] = ingredients[len(ingredients) - 1][: len(ingredients[len(ingredients) - 1]) - 1]
		contents = q.contents
		picture = q.picture
		date = q.datePosted
		print(ingredients)
		return render(request, 'recipeblog/recipedetail.html', {'title': title, 'postedBy': postedBy, 'ingredients': ingredients, 'contents': contents, 'picture': picture, 'datePosted': date})

