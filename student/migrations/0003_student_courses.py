# Generated by Django 5.0.7 on 2024-08-11 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_remove_course_id_remove_course_student_and_more'),
        ('student', '0002_alter_student_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(to='course.course'),
        ),
    ]