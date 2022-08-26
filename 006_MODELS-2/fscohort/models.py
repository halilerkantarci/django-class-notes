from django.db import models


class Student(models.Model):
    first_name = models.CharField("Adı",max_length=50)
    last_name = models.CharField("Soyadı",max_length=50)
    number = models.IntegerField("Numara")
    
    
    def __str__(self):
        return f"{self.number}-{self.first_name} {self.last_name}"
    
    class Meta:
        ordering = ["number"]  # "-number" yaparsan tersten sıralar
        verbose_name_plural = "Öğrenciler"