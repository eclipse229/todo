from django.contrib import admin
from .models import Checker
# Register your models here.
@admin.register(Checker)

class CheckerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date','related_to_person',
                    'related_to_place', 'status')
    list_filter = ('status', 'id', 'title', 'date')
    search_fields = ('title', 'activity_note')
    prepopulated_fields = {'title': ('title',)}
    date_hierarchy = 'date'
    ordering = ('id','title')
