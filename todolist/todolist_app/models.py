from django.db import models


class Task(models.Model):
    STATUS_DRAFT = 'DRAFT'
    STATUS_PUBLISHED = 'PUBLISHED'

    class Completed(models.TextChoices):
        YES = 'COMPLETED'
        NO = 'IN PROGRESS'

    STATUSES = (
        (STATUS_DRAFT, 'draft'),
        (STATUS_PUBLISHED, 'published'),
    )
    name = models.CharField(max_length=150, default='no name', verbose_name='what to do (here keep long story really '
                                                                            'short)')
    description = models.TextField(null=True, blank=True, verbose_name='here get here into details if needed')
    due_date = models.DateTimeField(null=True, blank=True, verbose_name='due to')
    completed = models.CharField(
        choices=Completed.choices,
        default=Completed.NO
    )
    status = models.CharField(choices=STATUSES, default=STATUS_DRAFT, verbose_name='status', max_length=10)
    author = models.CharField(max_length=200, null=True, blank=True)
    tags = models.ManyToManyField('Tag', 'tasks')

    class Meta:
        verbose_name = 'TO-DO'
        verbose_name_plural = 'TO-DOs'


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.pk} on {self.created_at}'


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
