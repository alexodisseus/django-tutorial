from django.urls import path

from core import views

urlpatterns	= [
	path('list' , views.list , name='list'),
	path('' , views.list , name='home'),
	path('create' , views.create , name='create'),
	path('details/<int:id>' , views.details , name='details'),
	path('delete/<int:id>' , views.delete , name='delete'),
	path('update/<int:id>' , views.update , name='update'),

]