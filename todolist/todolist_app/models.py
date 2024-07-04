from django.db import models


class Task(models.Model):
    class Completed(models.TextChoices):
        YES = 'COMPLETED'
        NO = 'IN PROGRESS'

    name = models.CharField(max_length=150, verbose_name='what to do (here keep long story really short)')
    description = models.TextField(null=True, blank=True, verbose_name='here get here into details if needed')
    due_date = models.DateTimeField(null=True, blank=True, verbose_name='Due to')
    completed = models.CharField(
        choices=Completed.choices,
        default=Completed.NO
    )

    class Meta:
        verbose_name = 'TO-DO'
        verbose_name_plural = 'TO-DOs'
