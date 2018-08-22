from django.urls import path

from . import views

app_name = 'recipeblog'
urlpatterns = [
	path('', views.index, name='index'),
	#path('<recipe>/', views.recipe, name='recipe')
]