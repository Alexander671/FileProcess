from django.core.validators import FileExtensionValidator
from rest_framework import serializers

from .models import File
from core.settings import ALLOWED_EXTENSIONS, FILE_SIZE


# size
def validate_file_size(value):
    max_size = FILE_SIZE * 1024 * 1024
    if value.size > max_size:
        raise serializers.ValidationError("Размер файла превышает допустимый предел (10 МБ)")
    return value


class FileSerializer(serializers.ModelSerializer):
    file = serializers.FileField(max_length=100, validators=[FileExtensionValidator(ALLOWED_EXTENSIONS),
                                                             validate_file_size])

    class Meta:
        model = File
        fields = '__all__'
        read_only_fields = ('processed',)
