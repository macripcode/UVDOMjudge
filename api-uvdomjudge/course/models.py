# -*- coding: utf-8 -*-
import time
from django.db import models
from period.models import AcademicPeriod


CODE_SUBJECTS_CHOICES = (
    ('750001M', '750001M'),
    ('750017M', '750017M'),
)

NAMES_SUBJECTS_CHOICES = (
    ('Algoritmia y Programación', 'Algoritmia y Programación'),
    ('Métodos Numéricos', 'Métodos Numéricos'),
)

CREDITS_SUBJECTS_CHOICES = (
    ('3', '3'),
    ('4', '4'),
)

LANGUAGES_CHOICES = (
    ('1', 'Python'),
    ('2', 'Scilab'),
)

PERIOD_CHOICES = (
    ('01', 'February - June'),
    ('02', 'August - December'),
)

curren_year = time.strftime("%Y")
next_year = str(int(time.strftime("%Y")) + 1)

YEAR_CHOICES = (
    ('0', 'Choose your option'),
    (curren_year, curren_year),
    (next_year, next_year),
)


class Course(models.Model):
    id_course = models.CharField(max_length=50, primary_key=True)
    code_course = models.CharField(max_length=50, choices=CODE_SUBJECTS_CHOICES, default=0)
    name_course = models.CharField(max_length=250, choices=NAMES_SUBJECTS_CHOICES, default=0)
    credits_course = models.CharField(max_length=10, choices=CREDITS_SUBJECTS_CHOICES, default=0)
    professor_course = models.CharField(max_length=50)
    group_course = models.CharField(max_length=50)
    programming_language = models.CharField(max_length=250, choices=LANGUAGES_CHOICES, default=0)
    period_course = models.CharField(max_length=250, choices=PERIOD_CHOICES, default=0)
    year_course = models.CharField(max_length=50, choices=YEAR_CHOICES, default=0)
    academic_period = models.ForeignKey(AcademicPeriod, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_course
