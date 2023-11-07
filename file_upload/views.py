from rest_framework import status, viewsets, mixins
from rest_framework.response import Response

from .serializers import FileSerializer
from .tasks import process_file


class FileViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = FileSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = serializer.save()
        process_file.delay(result.pk)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
