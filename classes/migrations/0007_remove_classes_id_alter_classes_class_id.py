# Generated by Django 5.0.7 on 2024-08-17 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0006_remove_classes_courses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classes',
            name='id',
        ),
        migrations.AlterField(
            model_name='classes',
            name='class_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
