from django.db import models
import uuid
# Create your models here.


def random_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = uuid.uuid4()
    return f'project/images/{filename}.{ext}'


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to=random_file_name)
    url = models.URLField()

    def __str__(self):
        return self.title
