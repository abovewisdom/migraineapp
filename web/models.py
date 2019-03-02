from django.db import models
from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User

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

class Migraines(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    mgstart_time = models.DateTimeField
    mgstart_stage = models.CharField(choices=MigraineStage.MIGRAINE_START_STATE_CHOICES, max_length = 40)
    mgstart_medicine = models.CharField(choices=MedicineChoices.MEDICINE_CHOICES, max_length = 40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('modelforms:index')
#class timecalc(models.Model):
#    todaydate = models.DateField(default=date.today)
#    todaytime = models.DateTimeField(detault=
