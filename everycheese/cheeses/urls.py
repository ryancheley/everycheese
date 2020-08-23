from django.urls import path
from .import views

app_name = "cheeses"

urlpatterns = [
    path(route='', view=views.CheeseListView.as_view(), name="list"),
    path(route='create/new/', view=views.CheeseCreateView.as_view(), name="create"),
    path(route='<slug:slug>', view=views.CheeseDetailView.as_view(), name="detail"),
]