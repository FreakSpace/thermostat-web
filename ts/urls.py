from django.urls import path
from .views.home import DataListView
from .views.all_records import AllDataView, GetSingle

urlpatterns = [
    path('', DataListView.as_view(), name='home'),
    path('all_data/single/', GetSingle.as_view(), name='single'),
    path('all_data/', AllDataView.as_view(), name='all-data'),
]
