# Generated by Django 5.0.6 on 2024-07-20 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0006_tag_task_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='get into details if needed ...'),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(default='no name', max_length=150, verbose_name='what to do?'),
        ),
    ]
