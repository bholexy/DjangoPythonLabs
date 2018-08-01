from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('notes/<post_id>', views.notes, name='notes'),
]