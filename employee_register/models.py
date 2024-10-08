from django.db import models
import uuid

class Position(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.title
    
class Employee(models.Model):
    id = models.UUIDField(primary_key= True, default=uuid.uuid4, editable=True)
    fullname = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    emp_code = models.CharField(max_length=3)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
