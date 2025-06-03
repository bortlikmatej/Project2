from django.urls import path 
from . import views
from .views import gallery_view

urlpatterns = [
    path('', views.index, name='index'),
    path('gallery/', gallery_view, name='gallery'),
]