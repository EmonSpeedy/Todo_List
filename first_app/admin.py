from django.contrib import admin
from first_app.models import TaskModel
# Register your models here.
class TaskModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'is_completed']

admin.site.register(TaskModel, TaskModelAdmin)

# class CompleteModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title', 'description', 'is_completed']
    
# admin.site.register(CompleteModel, CompleteModelAdmin)

