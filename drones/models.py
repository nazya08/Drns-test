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
    name = models.CharField("Модель", max_length=255, unique=True)
    description = models.TextField("Опис")
    priority = models.CharField(
        "Пріорітет", max_length=20, choices=[(tag.name, tag.value) for tag in Priority]
    )
    status = models.CharField(
        "Статус", max_length=20, choices=[(tag.name, tag.value) for tag in Status], default=Status.ACTIVE.value
    )

    class Meta:
        verbose_name = 'Дрон'
        verbose_name_plural = 'Дрони'
        ordering = ('status', 'priority')

    def __str__(self):
        return f'{self.name} ({self.pk})'
