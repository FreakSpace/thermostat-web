from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Thermostat(models.Model):
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

    time = models.DateTimeField(auto_now_add=True)

    for_program = models.BooleanField("Для використання програмою", default=False)

    def __str__(self):
        return f"{self.time.strftime('%Y-%m-%d %H:%M:%S')} | State: {'On' if self.thermostat_state else 'Off'} | t: {self.temp}" \
               f"{' | light:' + str(self.light) if self.light else ''}"


class Program(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=1000, blank=True, null=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class FieldProgram(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    thermostat_state = models.BooleanField("Стан термостату", default=False)
    set_temp = models.FloatField("Встановити температура", default=0)
    set_co2 = models.FloatField("Встановити рівень CO2", blank=True, null=True)
    light = models.BooleanField("Стан освітлення", default=False)

    light_R = models.IntegerField("R", default=0)
    light_G = models.IntegerField("G", default=0)
    light_B = models.IntegerField("B", default=0)

    duration = models.CharField("Тривалість виконання частини програми", max_length=20, default="")
    def __str__(self):
        return f"{self.program} | {self.field}"


class LogUseProgram(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)