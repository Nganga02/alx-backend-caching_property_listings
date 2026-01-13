from django.db import models
import uuid

class Property(models.Model):
    id=models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
                        )
    title=models.CharField(max_length=200)
    description=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    location=models.CharField(max_length=100)
    created_at=models.DateTimeField()

    def __str__(self):
        return f'{self.title}'