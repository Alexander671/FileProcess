from django.db import models


def path_generator(instance: models.Model, filename: str) -> str:
    ext = filename.split('.')[-1]
    filename = f'{instance.id}.{ext}'
    return f'uploads/{instance.__class__.__name__}/{filename[2:3]}/{filename}'
