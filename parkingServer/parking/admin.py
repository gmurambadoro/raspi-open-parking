from django.contrib import admin

from .models import Gate, Movement, Product


@admin.register(Gate)
class GateAdmin(admin.ModelAdmin):
    list_display = ('name', 'direction',)
    search_fields = ('name', 'direction',)
    list_filter = ('direction',)


@admin.register(Movement)
class MovementAdmin(admin.ModelAdmin):
    list_display = ('reference_number', 'entrance_datetime', 'entrance_gate', 'exit_gate', 'exit_datetime', 'status',)
    search_fields = ('reference_number', 'entrance_gate__name', 'exit_gate__name',)


@admin.register(Product)
class ParkingAdmin(admin.ModelAdmin):
    list_display = ('name', 'rate',)
    search_fields = ('name',)
    list_filter = ('rate',)
