from django.urls import path
from django.views.generic import TemplateView

from . import views
app_name = 'nutritiontracker'
urlpatterns = [
    path('', views.renderAll, name='renderAll'),
    path('404.html', TemplateView.as_view(template_name="404.html"), name='error'),
    path('updatedetails', views.updateDetails, name='updateDetails'),
    path('submitfood', views.submitFood, name='submitFood'),
]