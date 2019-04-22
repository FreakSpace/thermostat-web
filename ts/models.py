from django.db import models


class LogThermostat(models.Model):
    thermostat_state = models.BooleanField("Стан термостату", default=False)
    current_state = models.CharField("Стан термостату", max_length=20)

    temp = models.FloatField("Температура", default=0)
    set_temp = models.FloatField("Встановлена температура", default=0)

    co2 = models.FloatField("Рівень CO2", blank=True, null=True)
    set_co2 = models.FloatField("Встановлений рівень CO2", blank=True, null=True)

    light = models.BooleanField("Стан освітлення", default=False)

    light_R = models.IntegerField("R", default=0)
    light_G = models.IntegerField("G", default=0)
    light_B = models.IntegerField("B", default=0)

    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.time.strftime('%Y-%m-%d %H:%M:%S')} | State: {'On' if self.thermostat_state else 'Off'} | t: {self.temp}" \
               f"{' | light:' + str(self.light) if self.light else ''}"
