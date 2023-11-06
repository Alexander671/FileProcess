from django.db import models
from common.models import path_generator


class File(models.Model):
    file = models.FileField('File', upload_to=path_generator)
    uploaded_at = models.DateTimeField('Uploaded at', auto_now_add=True)
    processed = models.BooleanField('Proccessed', default=False)

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'
