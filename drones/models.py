from enum import Enum

from django.db import models


class Priority(Enum):
    HIGH = 'Високий'
    MEDIUM = 'Нормальний'
    LOW = 'Низький'


class Status(Enum):
    ACTIVE = 'Актуально'
    INACTIVE = 'Неактуально'


class Drone(models.Model):
    name = models.CharField("Model", max_length=255, unique=True)
    description = models.TextField("Description")
    priority = models.CharField(
        "Priority", max_length=20, choices=[(tag.name, tag.value) for tag in Priority]
    )
    status = models.CharField(
        "Status", max_length=20, choices=[(tag.name, tag.value) for tag in Status], default=Status.ACTIVE.value
    )

    class Meta:
        verbose_name = 'Drone'
        verbose_name_plural = 'Drones'
        ordering = ('status', 'priority')

    def __str__(self):
        return f'{self.name} ({self.pk})'


class DronePart(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class DroneDronePart(models.Model):
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)
    drone_part = models.ForeignKey(DronePart, on_delete=models.CASCADE)
    count = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f'Дрон: {self.drone} Деталь: {self.drone_part} кількість: {self.count}'
