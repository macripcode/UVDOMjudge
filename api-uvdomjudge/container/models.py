from django.db import models
from course.models import Course


class Container(models.Model):
        associated_course = models.ForeignKey(Course, on_delete=models.CASCADE)
        id_container = models.CharField(max_length=250, primary_key=True)
        name_container = models.CharField(max_length=250)
        port_number_80_container = models.CharField(max_length=50)
        port_number_3306_container = models.CharField(max_length=50)
        base_image_container = models.CharField(max_length=250)
        address_volume_db_host_container = models.CharField(max_length=250)
        ip_address_container = models.CharField(max_length=250)
        running_container = models.CharField(max_length=250)

        def __str__(self):
            return self.id_container



