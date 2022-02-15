from django.urls import path
from . import views
from rest_framework import routers
from django.conf.urls import include


urlpatterns = [
	path('', views.getPage, name="page"),
  path('<str:pk>', views.getPageId, name="pageId"),

	path('create/', views.createPage, name="create-page"),
	path('update/<str:pk>/', views.updatePage, name="create-page"),
	path('delete/<str:pk>/', views.deletePage, name="create-page"),

  # path('notes/<str:pk>/update/', views.updateNote, name="update-note"),
  # path('notes/<str:pk>/delete/', views.deleteNote, name="delete-note"),


]