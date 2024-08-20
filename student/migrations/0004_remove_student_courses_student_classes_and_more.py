# Generated by Django 5.0.7 on 2024-08-17 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0006_remove_classes_courses'),
        ('course', '0005_remove_course_course_id_course_id_and_more'),
        ('student', '0003_student_courses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='courses',
        ),
        migrations.AddField(
            model_name='student',
            name='classes',
            field=models.ManyToManyField(related_name='students', to='classes.classes'),
        ),
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.ManyToManyField(related_name='students', to='course.course'),
        ),
    ]
