from django.db import models

DIRECTION_CHOICES = [
    ('NONE', 'NONE'),
    ('IN', 'IN'),
    ('OUT', 'OUT'),
    ('IN_OUT', 'IN & OUT'),
]


class Gate(models.Model):
    """Gate represents an entry or exit configuration"""
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    direction = models.CharField(max_length=10, choices=DIRECTION_CHOICES,
                                 default=DIRECTION_CHOICES[0][0], null=False, blank=False)

    def __str__(self):
        return f'{self.name} : {self.get_direction_display()}'
