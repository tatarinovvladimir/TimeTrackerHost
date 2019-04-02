# Generated by Django 2.1.5 on 2019-03-25 20:29

import datetime
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comm_text', models.TextField(max_length=500)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='JournalPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_date', models.DateTimeField(default=datetime.datetime.now)),
                ('used_time', models.FloatField(null=True)),
                ('post_text', models.TextField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='NewsPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('text', models.TextField(max_length=1000)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('actual_time', models.IntegerField(blank=True, null=True)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts_manager.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('short_description', models.CharField(max_length=100, null=True)),
                ('full_description', tinymce.models.HTMLField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Author', to='accounts_manager.Profile')),
                ('developers', models.ManyToManyField(related_name='Developers', to='accounts_manager.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=400)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('task_type', models.CharField(max_length=50)),
                ('priority', models.CharField(choices=[('Normal', 'Normal'), ('High', 'High'), ('Extra', 'Extra')], max_length=50)),
                ('estimated_time', models.FloatField(verbose_name='Estimated time in hours')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts_manager.Profile')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='mainApp.Project')),
            ],
        ),
        migrations.AddField(
            model_name='journalpost',
            name='for_task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainApp.Task'),
        ),
        migrations.AddField(
            model_name='journalpost',
            name='made_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts_manager.Profile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_for',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainApp.Task'),
        ),
        migrations.AddField(
            model_name='comment',
            name='commentator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts_manager.Profile'),
        ),
    ]