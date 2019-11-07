from datetime import datetime, timedelta
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
    paginate_by = 60
    queryset = Thermostat.objects.all().order_by('-time')

    def __init__(self, *args, **kwargs):
        data = super().__init__(*args, **kwargs)
        self.all_records_number = 0

    @staticmethod
    def _range_date(start_date_text=None, end_date_text=None, first_record_date=None, last_record_date=None):
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
            start_date = datetime.strptime(first_record_date.strftime('%Y-%m-%d-%H-%M'), "%Y-%m-%d-%H-%M")
            end_date = datetime.strptime(last_record_date.strftime('%Y-%m-%d-%H-%M'), "%Y-%m-%d-%H-%M")

        return start_date, end_date

    def get_queryset(self):
        start_date_text = self.request.GET.get("start_date")
        end_date_text = self.request.GET.get("end_date")
        ts_state = self.request.GET.get("ts_state")
        current_state = self.request.GET.get("current_state")
        light_state = self.request.GET.get("light_state")

        qset = self.queryset

        first_record_date = qset.reverse().first().time
        last_record_date = qset.reverse().last().time
        start_date, end_date = self._range_date(start_date_text, end_date_text, first_record_date, last_record_date)

        if start_date >= end_date:
            data = qset.filter(time__range=(None, None))
        else:
            data = qset.filter(time__range=(start_date, end_date))

        if ts_state and ts_state != "2":
            data = data.filter(thermostat_state=int(ts_state))

        if current_state and current_state != "3":  # 0 - вимк, 1 - тепло, 2 - охолодження, 3 - всі зразу
            data = data.filter(current_state=current_state)

        if light_state and light_state != "4":
            data = data.filter(light=int(light_state))

        self.all_records_number = len(data)

        return data

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)

        filter_by_date = self.request.GET.get("filter_by_date")
        start_date_text = self.request.GET.get("start_date")
        end_date_text = self.request.GET.get("end_date")
        ts_state = self.request.GET.get("ts_state")
        current_state = self.request.GET.get("current_state")
        light_state = self.request.GET.get("light_state")

        qset = self.queryset
        first_record_date = qset.reverse().first().time
        last_record_date = qset.reverse().last().time
        start_date, end_date = self._range_date(start_date_text, end_date_text, first_record_date, last_record_date)

        data['filter_by_date'] = filter_by_date
        data['start_date'] = start_date
        data['end_date'] = end_date
        data['ts_state'] = ts_state
        data['current_state'] = current_state
        data['light_state'] = light_state

        data['all_records_number'] = self.all_records_number


        if start_date >= end_date:
            data['alert_code'] = 0
            data['alerts'] = "Початкова дата та час не можуть бути більшими за кінцеві!"

        elif not self.all_records_number:
            data['alert_code'] = 1
            data['alerts'] = "З такими параметрами записів не знайдено"

        return data