from django.urls import path

from . import views
#urls for various views
urlpatterns = [
    path('', views.api_home)
]