from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField('Имя', max_length=50)
    task = models.CharField('Номер', max_length=50)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Список'
