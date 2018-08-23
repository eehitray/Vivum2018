from django.urls import path
from django.views.generic import TemplateView

from . import views
app_name = 'nutritiontracker'
urlpatterns = [
    path('', views.renderAll, name='renderAll'),
]