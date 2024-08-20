# Generated by Django 5.0.7 on 2024-08-11 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_remove_course_id_remove_course_student_and_more'),
        ('teacher', '0004_alter_teacher_teacher_headshot'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='student',
        ),
        migrations.AddField(
            model_name='teacher',
            name='courses',
            field=models.ManyToManyField(to='course.course'),
        ),
    ]