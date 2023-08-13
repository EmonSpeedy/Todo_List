from django import forms
from . models import TaskModel

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['title', 'description']
        
# class CompleteForm(forms.ModelForm):
#     class Meta:
#         model = CompleteModel
#         fields = '__all__'
