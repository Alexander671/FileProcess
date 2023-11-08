import uuid

from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse


class BaseAbstractModel(models.Model):
    """ Base timestamp abstract model """
    uid = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    modified_at = models.DateTimeField('Изменено', auto_now=True)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f'{self.__class__.__name__} | {self.str_data()}'

    def str_data(self) -> str:
        return self.pk

    @classmethod
    def get_admin_url(cls) -> str:
        """Get relative reference to list"""
        content_type = ContentType.objects.get_for_model(cls)
        return reverse(f'admin:{content_type.app_label}_{content_type.model}_changelist')


def path_generator(instance: BaseAbstractModel, filename: str) -> str:
    ext = filename.split('.')[-1]
    filename = f'{instance.uid}.{ext}'
    return f'uploads/{instance.__class__.__name__}/{filename[2:3]}/{filename}'
