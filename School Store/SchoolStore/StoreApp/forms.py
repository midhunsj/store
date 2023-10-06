from django import forms
from .models import Department,Courses

class StoreForm(forms.Form):
    name=forms.CharField(max_length=50)
    department=forms.ModelChoiceField(queryset=Department.objects.all())
    course=forms.ModelChoiceField(queryset=Courses.objects.none())
