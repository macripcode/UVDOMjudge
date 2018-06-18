from django.db import models



class AcademicPeriod(models.Model):

    id_academic_period = models.CharField(max_length=250, primary_key=True)
    name_academic_period = models.CharField(max_length=250)

    def __str__(self):
        return self.name_academic_period

