# Generated by Django 5.0.7 on 2024-08-17 16:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classes', '0007_remove_classes_id_alter_classes_class_id'),
        ('teacher', '0007_remove_teacher_id_alter_teacher_teacher_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField()),
                ('course', models.CharField(max_length=100)),
                ('classroom', models.CharField(max_length=100)),
                ('day_of_the_week', models.IntegerField()),
                ('classes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.classes')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher')),
            ],
        ),
    ]
