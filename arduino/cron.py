from django_cron import CronJobBase, Schedule
from .serial_read import get_data_from_box


class GetData(CronJobBase):
    RUN_EVERY_MINS = 2 # every 2 hours

    schedule = Schedule(run_every_mins=1)
    code = 'arduino.cron'    # a unique code

    def do(self):
        # get_data_from_box()
        print("tut")