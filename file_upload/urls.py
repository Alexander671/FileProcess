from django.urls import path

from .views import FileViewSet

urlpatterns = [
    path('', FileViewSet.as_view({'get': 'list'})),
    path('upload/', FileViewSet.as_view({'post': 'create'}), name='file-upload'),
]
