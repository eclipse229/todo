from django.urls import path
from . import views

#urls for the checker application

app_name ='checker'
urlpatterns = [
    path('', views.ListViews.as_view(), name='list'),
    path('<int:id>/<title>/details/', views.details, name='details'),
]
