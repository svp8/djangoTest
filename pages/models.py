from django.db import models

# Create your models here.
class Person(models.Model):
    def __str__(self) -> str:
        return self.first_name

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active=models.BooleanField(default=True)
    date_birth=models.DateField(blank=True,null=True)
    department=models.ForeignKey("Department", on_delete=models.CASCADE,null=True)
    tasks=models.ManyToManyField("Task",blank=True)
class Department(models.Model):
    def __str__(self) -> str:
        return self.name
    name = models.CharField(max_length=30)
class Task(models.Model):
    def __str__(self) -> str:
        return self.name
    name = models.CharField(max_length=30)
    


