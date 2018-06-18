from django.db import models


class Image(models.Model):
    id_image = models.CharField(max_length=50, primary_key=True)
    name_image = models.CharField(max_length=50)
    language_image = models.CharField(max_length=50)

    def __str__(self):
        return self.name_image


# a = Image(id_image = '1', name_image = 'uv-domjudge-python:1.0',language_image = 'python' )
# a.save()
# b = Image(id_image = '2', name_image = 'uv-domjudge-scilab:1.0',language_image = 'scilab' )
# b.save()