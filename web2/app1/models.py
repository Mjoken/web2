from django.db import models


class StudySession(models.Model):
    group = models.CharField(max_length=10)
    title = models.CharField(max_length=255)
    short_title = models.CharField(default="Мат.Анализ", max_length=10, blank=True, null=True)
    session_type = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    subgroup = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    comment = models.TextField(default="Здесь могла быть ваша заметка", blank=True, null=True)
    date_start = models.DateField(auto_now_add=True, blank=True)
    time_start = models.TimeField(auto_now_add=True, blank=True)

    def get_group(self):
        return self.group

    def get_group_filtered(self):
        group_filtered = str(self.group).lower().replace('-', '')
        return group_filtered
