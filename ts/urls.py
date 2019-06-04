from django.urls import path
from .views.home import DataListView
from .views.all_records import AllDataView, get_single
from .views.userprofile import UserProfileView
from .views.programs import ProgramsView, SingleProgramView, run_program


urlpatterns = [
    path('', DataListView.as_view(), name='home'),

    path('all_data/single/', get_single, name='single'),
    path('all_data/', AllDataView.as_view(), name='all-data'),

    path('programs/id<int:pk>', SingleProgramView.as_view(), name='single-program'),
    path('programs/add_phase', ProgramsView.as_view(), name='programs'),
    path('programs/run/', run_program, name='run-program'),
    path('programs/', ProgramsView.as_view(), name='programs'),

    path('user/id<int:pk>', UserProfileView.as_view(), name='user-profile'),
]

