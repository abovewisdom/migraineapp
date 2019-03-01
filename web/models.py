from django.db import models
from datetime import date


class MigraineStage(models.Model):
    BEFORESTART = 'start'
    EARLY  = 'early'
    LATE = 'late'
    MIGRAINE_START_STATE_CHOICES = (
        (BEFORESTART, 'Before Start'),
        (EARLY, 'Early'),
        (LATE, 'Late'),
    )

class MedicineChoices(models.Model):
    ADVIL = 'advil'
    MAXALT  = 'maxalt'
    IMITREX = 'imitrex'
    MEDICINE_CHOICES = (
        (ADVIL, 'Advil'),
        (MAXALT, 'Maxalt'),
        (IMITREX, 'Imitrex'),
    )

#class timecalc(models.Model):
#    todaydate = models.DateField(default=date.today)
#    todaytime = models.DateTimeField(detault=
