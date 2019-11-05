from django.views.generic import ListView
from ts.models import Thermostat
from django.http import JsonResponse


def get_single(request):
    data = {}
    id_elem = request.GET.get('id')
    record = Thermostat.objects.get(id=id_elem)
    data["date"] = record.time.strftime('%H:%M | %d-%m-%Y')
    data["id"] = record.id
    data["thermostat_state"] = record.thermostat_state
    data["current_state"] = record.current_state
    data["temp"] = record.temp
    data["set_temp"] = record.set_temp
    data["co2"] = record.co2
    data["set_co2"] = record.set_co2
    data["light"] = record.get_light_mode()
    data["light_UV"] = record.light_UV
    data["light_R"] = record.light_R
    data["light_G"] = record.light_G
    data["light_B"] = record.light_B
    return JsonResponse(data)


class AllDataView(ListView):
    model = Thermostat
    template_name = "ts/all_data.html"
    context_object_name = 'records'
    paginate_by = 50
    queryset = Thermostat.objects.all().order_by('-time')