from django.db import models


class LogThermostat(models.Model):
    temp = models.FloatField("Температура")
    co2 = models.FloatField("CO2", blank=True, null=True)

    on = models.BooleanField("On")

    current_state = models.CharField("Стан термостату", max_length=20)

    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.time.strftime('%Y-%m-%d %H:%M:%S')} | State: {'On' if self.on else 'Off'} | t: {self.temp}" \
               f"{' | co2:' + str(self.co2) if self.co2 else ''}"
