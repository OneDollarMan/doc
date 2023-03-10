import uuid
from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Document(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='files/', default=None)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.title




