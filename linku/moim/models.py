from django.db import models


class Meeting(models.Model):
    maker = models.TextField()
    name = models.TextField()
    place = models.TextField()
    start_time = models.DateTimeField()
    image_path = models.ImageField(blank=True)
    distance_near_univ = models.TextField()
    price_range = models.TextField()


class RunPythonExample(models.Model):
    test_name = models.TextField()
    test_text = models.TextField()
