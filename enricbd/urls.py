from django.urls import path,include
from . import views


urlpatterns = [
    path('enric', views.EnricApi.as_view()),
]
