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
			return blog(request, recipename)
	else: 
		return render(request, '404.html')

def blog(request, rname):
	try:
		q = Post.objects.get(title = rname)
	except:
		return render(request, '404.html')
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

def sbName(request):
	if (request.POST):
		rname= request.POST['rsName']
	
		q = Post.objects.filter(title__icontains=rname)
		if (len(q) == 0 or rname==''):
			return render(request, 'recipeblog/index.html', {'text': 'No such recipes were found.'})
		else:
			return render(request, 'recipeblog/index.html', {'lastRecipes': q, 'text': 'Search results for ' + rname})
	else:
		return render(request, '404.html')

def sbIngredients(request):
	if (request.POST):
		ingredients = request.POST['rsIng']
		l = Post.objects.order_by('title')
		ln = []
		for i in l:
			flag = 1
			k = i.getIngredientsList()[1:len(i.getIngredientsList()) - 1].split(', ')
			for j in ingredients.split(', '):
				if j not in k:
					flag = 0
					break
			if (flag):
				ln.append(i)
		if (len(ln) == 0):
			return render(request, 'recipeblog/index.html', {'text': 'No such recipes were found.'})
		else:
			return render(request, 'recipeblog/index.html', {'lastRecipes': ln, 'text': 'Search results for the given ingredients'})
	else:
		return render(request, '404.html')