from django.views.generic import ListView
from ts.models import Program, FieldProgram


def create_or_edit_program(request):
    pass


class ProgramListView(ListView):
    context_object_name = "qset"
    model = Program
    template_name = 'ts/index.html'
    queryset = Program.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)

        data["programs"] = self.queryset

        return data

