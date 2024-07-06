# Generated by Django 5.0.6 on 2024-07-05 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0005_remove_task_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='tags',
            field=models.ManyToManyField(related_name='tasks', to='todolist_app.tag'),
        ),
    ]