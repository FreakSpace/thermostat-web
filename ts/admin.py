from django.contrib import admin
from .models import Thermostat, Program, Phase


admin.site.register(Thermostat)
admin.site.register(Program)
admin.site.register(Phase)
