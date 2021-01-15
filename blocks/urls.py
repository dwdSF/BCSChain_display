from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blocks/<int:block_height>/', views.block_view, name='block'),
]
