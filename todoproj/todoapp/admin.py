from django.contrib import admin
from .models import TodoModel
# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'phone', 'address']

    class Meta:
        ordering = ['id']


admin.site.register(TodoModel, TodoAdmin)
