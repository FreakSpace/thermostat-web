from django.urls import path
from .views import DataListView

urlpatterns = [
    path('', DataListView.as_view()),
]
