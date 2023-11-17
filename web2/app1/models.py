from django.db import models


class StudySession(models.Model):
    group = models.CharField(max_length=10)
    title = models.CharField(max_length=255)
    short_title = models.CharField(max_length=10)
    session_type = models.PositiveSmallIntegerField(default=0)
    subgroup = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True)
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
