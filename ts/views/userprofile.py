from django.views.generic import DetailView
from ts.models import User, Program, Phase, LogUseProgram


class UserProfileView(DetailView):
    model = User
    template_name = "ts/userprofile.html"
