from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('index.html', TemplateView.as_view(template_name="index.html"), name='mainIndex'),
    #path('test/', views.test_view, name='test')
]