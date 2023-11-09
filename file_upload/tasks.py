from celery import shared_task

from PIL import Image

from .models import File
from core.settings import MEDIA_ROOT


def confirm_processed_file(file_obj):
    file_obj.processed = True
    file_obj.save()


def handler_py(file_obj,):
    confirm_processed_file(file_obj)


def handler_txt(file_obj,):
    confirm_processed_file(file_obj)


def handler_jpg(file_obj,):
    file_path = f'{MEDIA_ROOT}/{file_obj.file}'
    jpg_image = Image.open(file_path)
    new_image = jpg_image.rotate(90)
    new_image.save(file_path, optimize=True, quality=95)
    confirm_processed_file(file_obj)


def handler_pass(file_obj,):
    pass


@shared_task
def process_file(file_id):
    file = File.objects.get(pk=file_id)
    file_extension = file.file.name.split('.')[-1]
    handler_func = globals().get('handler_' + file_extension, handler_pass)
    handler_func(file)
