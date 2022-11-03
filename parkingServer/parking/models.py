import datetime
import uuid

from django.core import validators
from django.db import models

DIRECTION_CHOICES = [
    ('NONE', 'NONE'),
    ('IN', 'IN'),
    ('OUT', 'OUT'),
    ('IN_OUT', 'IN & OUT'),
]

pin_validators = (validators.MinValueValidator(0), validators.MaxValueValidator(100),)


class Gate(models.Model):
    """Gate represents an entry or exit configuration"""
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    direction = models.CharField(max_length=10, choices=DIRECTION_CHOICES,
                                 default=DIRECTION_CHOICES[0][0], null=False, blank=False)
    sensor_presence_detector_pin = models.PositiveIntegerField(default=0, db_column='sensor_presence_detector_pin',
                                                               verbose_name='Presence detector pin',
                                                               validators=pin_validators,
                                                               help_text='Pin number of the sensor (e.g. push button) '
                                                                         'that indicates presence of an object at the '
                                                                         'gate e.g. vehicle')
    sensor_barrier_open_pin = models.PositiveIntegerField(default=0, db_column='sensor_barrier_open_pin',
                                                          verbose_name='Sensor pin for barrier opening',
                                                          validators=pin_validators,
                                                          help_text='Pin number of sensor (e.g. push button) that '
                                                                    'indicates '
                                                                    'that the boom needs to be opened')
    relay_open_barrier_pin = models.PositiveIntegerField(default=0, db_column='relay_open_barrier_pin',
                                                         verbose_name='Barrier open trigger relay pin',
                                                         validators=pin_validators,
                                                         help_text='Pin number of the relay that triggers the opening '
                                                                   'of the '
                                                                   'boom under normal operation')

    class Meta:
        verbose_name = 'Gate configuration'
        verbose_name_plural = 'Gate configurations'

    def __str__(self):
        return f'{self.name} : {self.get_direction_display()}'


class Movement(models.Model):
    """Represents an entry or exit via any one of the configured gates"""
    reference_number = models.CharField(max_length=50, unique=True, null=False, blank=False,
                                        editable=False,
                                        default=lambda: str(uuid.uuid4()),
                                        verbose_name='Barcode')
    entrance_gate = models.ForeignKey(Gate, on_delete=models.CASCADE, null=False, related_name='entrance_gates')
    entrance_datetime = models.DateTimeField(null=False, blank=False, default=datetime.datetime.now)
    exit_gate = models.ForeignKey(Gate, on_delete=models.CASCADE, null=True, related_name='exit_gates', blank=True)
    exit_datetime = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Movement entry'
        verbose_name_plural = 'Movement entries'

    def __str__(self):
        return f'{self.reference_number}'

    def status(self):
        if isinstance(self.exit_datetime, datetime.datetime) or isinstance(self.exit_gate, Gate):
            return 'OUT'
        return 'IN'
