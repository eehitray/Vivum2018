from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'recipeblog'
urlpatterns = [
	path('', views.index, name='index'),	
    path('index.html', TemplateView.as_view(template_name="index.html"), name='mainIndex'),
    path('form.html', TemplateView.as_view(template_name="recipeblog/form.html"), name='form'),
	path('submit', views.submit, name='submit'),
	path('<rname>', views.blog, name='blog'),
	path('search/name/', views.sbName, name='searchName'),
	path('search/ingredients/', views.sbIngredients, name='searchIngredients'),
]