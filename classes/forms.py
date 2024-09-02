from django import forms
from .models import Classes


class ClassesRegistationForm(forms.ModelForm):
    class Meta:
        model=Classes
        fields=["class_rules","class_capacity","class_performance","class_lecture","class_name","class_representative","class_description","class_table_number","class_bio","class_rules"]