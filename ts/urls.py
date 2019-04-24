from django.urls import path
from .views.home import DataListView
from .views.all_records import AllDataView, get_single

urlpatterns = [
    path('', DataListView.as_view(), name='home'),
    path('all_data/single/', get_single, name='single'),
    path('all_data/', AllDataView.as_view(), name='all-data'),
]
