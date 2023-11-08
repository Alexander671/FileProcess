from django.db import models
from common.models import BaseAbstractModel, path_generator


class File(BaseAbstractModel):
    file = models.FileField('File', upload_to=path_generator)
    processed = models.BooleanField('Proccessed', default=False)

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'
