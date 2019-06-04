from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from ts.models import User, Program, Phase, LogUseProgram
from arduino.tsbox import ThermostatBox


class ProgramsView(ListView):
    model = Program
    template_name = "ts/programs.html"
    context_object_name = 'programs'


class SingleProgramView(DetailView):
    model = Program
    template_name = "ts/program.html"
    context_object_name = 'program'

    def get_context_data(self, **kwargs):
        context = super(SingleProgramView, self).get_context_data(**kwargs)

        context['phases'] = Phase.objects.filter(program=context["program"])
        return context


def add_phase(request):
    return 0


def run_program(request):

    id_elem = request.GET.get('run_id')
    program_text = "set_program\n"
    phases = Phase.objects.filter(program_id=id_elem)

    for phase in phases:
        program_text += str(phase.order_execution) + ": "
        program_text += str(phase.duration_d) + ", "
        program_text += str(phase.duration_h) + ", "
        program_text += str(phase.duration_m) + "; "
        program_text += str(phase.thermostat_state) + "; "
        program_text += str(phase.set_temp) + "; "
        program_text += str(phase.set_co2) + "; "
        program_text += str(phase.light) + ", "
        program_text += str(phase.light_mode) + ", "
        program_text += str(phase.light_R) + ", "
        program_text += str(phase.light_G) + ", "
        program_text += str(phase.light_B) + ";\n"

    try:
        ts_box = ThermostatBox()
        ts_box.send_data_to_box(program_text)
    except:
        return JsonResponse({"state": "error"})
    finally:
        return JsonResponse({"state": "success"})