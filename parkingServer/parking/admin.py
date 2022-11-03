from django.contrib import admin

from .models import Gate


@admin.register(Gate)
class GateAdmin(admin.ModelAdmin):
    list_display = ('name', 'direction')
    search_fields = ('name', 'direction')
    list_filter = ('direction',)

