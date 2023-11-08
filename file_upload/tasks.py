from celery import shared_task

from .models import File


@shared_task
def process_file(file_id):
    file = File.objects.get(pk=file_id)
    filename = file.file.split('.')[-1]

    if filename == '.txt':

        file.processed = True
        file.save()

    elif filename == '.jpg':
        file.processed = True
        file.save()

    elif filename == '.pdf':
        file.processed = True
        file.save()

    else:
        file.processed = False
        file.save()
