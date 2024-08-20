from django.db import models

# Create your models here.

class Classes(models.Model):
    class_rules=models.TextField(max_length=20)
    class_capacity=models.SmallIntegerField()
    class_performance=models.CharField(max_length=30)
    class_lecture=models.CharField(max_length=30)
    class_id=models.AutoField(primary_key=True)
    class_name=models.CharField(max_length=30)
    class_representative=models.CharField(max_length=30)
    class_description=models.TextField(max_length=30)
    class_table_number=models.SmallIntegerField()
    class_bio=models.CharField(max_length=30)
    class_rules=models.CharField(max_length=30)

    def __str__(self):
        return f"{self.class_bio} {self.class_description}"
