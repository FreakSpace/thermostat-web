from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from django.utils import timezone
from ts.models import User, Program, Phase, LogUseProgram
from arduino.tsbox import ThermostatBox
from django.views.generic.edit import CreateView, DeleteView, UpdateView


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

        context['active_phases'] = Phase.objects\
            .filter(program=context["program"])\
            .filter(is_active=True) \
            .order_by("order_execution")

        context['not_active_phases'] = Phase.objects\
            .filter(program=context["program"])\
            .filter(is_active=False)\
            .order_by("order_execution")

        return context


def create_phase(request):
    if request.method == "POST":
        phase_name = request.POST.get("phase_name")
        thermostat_state = request.POST.get("thermostat_state")
        set_t = request.POST.get("thermostat_state")


def run_program(request):
    """
    Відправляє до ящика код:
        Order; Days; Hours; Min; TS_STATE; SET_T; STATE_CO2; SET_CO2; LIGHT_STATE; UV; R; G; B;
    """
    id_elem = request.GET.get('run_id')
    stop_program = request.GET.get('stop')
    if not stop_program and id_elem:
        program = Program.objects.get(id=id_elem)

        program_text = "set_program\n"
        program_text += f"program_id: {id_elem};\n"
        program_text += f"repeating: {program.repeating};\n"
        phases = Phase.objects.filter(program_id=id_elem).order_by("order_execution")

        for phase in phases:
            program_text += str(phase.order_execution) + ";"
            program_text += str(phase.duration_d) + ";"
            program_text += str(phase.duration_h) + ";"
            program_text += str(phase.duration_m) + ";"
            program_text += str(int(phase.thermostat_state)) + ";"
            program_text += str(phase.set_temp) + ";"
            program_text += str(int(phase.co2_control)) + ";"
            program_text += str(phase.set_co2) + ";"
            program_text += str(phase.light) + ";"
            program_text += str(phase.light_UV) + ";"
            program_text += str(phase.light_R) + ";"
            program_text += str(phase.light_G) + ";"
            program_text += str(phase.light_B) + ";\n"

        try:
            ts_box = ThermostatBox()
            ts_box.send_data_to_box(program_text)
            del ts_box
        except:
            return JsonResponse({"state": "error"})
        finally:
            program.last_use = timezone.now()
            program.save(update_fields=["last_use"])
            return JsonResponse({"state": "success"})
    elif stop_program:
        try:
            ts_box = ThermostatBox()
            ts_box.send_data_to_box("stop")
            del ts_box
        except:
            return JsonResponse({"state": "error"})
        finally:
            return JsonResponse({"state": "success"})