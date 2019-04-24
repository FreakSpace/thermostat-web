from django.contrib import admin
from .models import Thermostat, UserProfile, Program, FieldProgram, LogUseProgram


admin.site.register(Thermostat)
admin.site.register(UserProfile)
admin.site.register(Program)
admin.site.register(FieldProgram)
admin.site.register(LogUseProgram)
