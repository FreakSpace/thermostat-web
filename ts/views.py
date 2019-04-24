from django.views.generic import ListView, CreateView
from .models import LogThermostat
from datetime import datetime, timedelta
from django.http import JsonResponse


def get_single(request):
    data = {}
    id_elem = request.GET.get('id')
    record = LogThermostat.objects.get(id=id_elem)
    data["date"] = record.time.strftime('%H:%M | %d-%m-%Y')
    data["id"] = record.id
    data["thermostat_state"] = record.thermostat_state
    data["current_state"] = record.current_state
    data["temp"] = record.temp
    data["set_temp"] = record.set_temp
    data["co2"] = record.co2
    data["set_co2"] = record.set_co2
    data["light"] = record.light
    data["light_R"] = record.light_R
    data["light_G"] = record.light_G
    data["light_B"] = record.light_B
    return JsonResponse(data)


class AllDataView(ListView):
    model = LogThermostat
    template_name = "ts/all_data.html"
    context_object_name = 'records'
    paginate_by = 50
    queryset = LogThermostat.objects.all().order_by('-time')


class DataListView(ListView):
    context_object_name = "qset"
    model = LogThermostat
    template_name = 'ts/index.html'
    queryset = LogThermostat.objects.all()

    def __init__(self):
        self.all_records_number = 0
        self.got_records_number = 0
        self.step_record = 0

    def _range_date(self, start_date_text=None, end_date_text=None):
        if start_date_text and end_date_text:
            start_date = datetime.strptime(start_date_text, "%Y-%m-%d-%H-%M")
            end_date = datetime.strptime(end_date_text, "%Y-%m-%d-%H-%M")

        elif start_date_text and not end_date_text:
            start_date = datetime.strptime(start_date_text, "%Y-%m-%d-%H-%M")
            end_date = datetime.now()

        elif not start_date_text and end_date_text:
            end_date = datetime.strptime(end_date_text, "%Y-%m-%d-%H-%M")
            start_date = end_date - timedelta(hours=1)

        else:
            start_date = datetime.today() - timedelta(hours=1)
            end_date = datetime.now()

        return start_date, end_date

    def get_queryset(self):
        start_date_text = self.request.GET.get("start_date")
        end_date_text = self.request.GET.get("end_date")
        to_reduce = True if self.request.GET.get("to_reduce") == 'true' else False

        start_date, end_date = self._range_date(start_date_text, end_date_text)
        if start_date >= end_date:
            data = self.queryset.filter(time__range=(None, None))
        else:
            data = self.queryset.filter(time__range=(start_date, end_date))

        self.all_records_number = len(data)
        if self.all_records_number > 60 and to_reduce:
            self.step_record = round(len(data) / 60)
            data = data[::self.step_record]
            self.got_records_number = len(data)
        else:
            self.step_record = 1
            self.got_records_number = self.all_records_number

        return data

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)

        start_date_text = self.request.GET.get("start_date")
        end_date_text = self.request.GET.get("end_date")

        start_date, end_date = self._range_date(start_date_text, end_date_text)
        data['start_date'] = start_date
        data['end_date'] = end_date


        data['last_record'] = self.queryset.last()

        data['all_records_number'] = self.all_records_number
        data['got_records_number'] = self.got_records_number
        data['step_record'] = self.step_record

        if start_date >= end_date:
            data['alert_code'] = 0
            data['alerts'] = "Початкова дата та час не можуть бути більшими за кінцеві. <strong>Вибрано дані за останню годину</strong>"

        elif not self.all_records_number:
            data['alert_code'] = 1
            data['alerts'] = "В даний період часу немає записів"

        return data


