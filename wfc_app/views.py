from django.shortcuts import render
from rest_framework.parsers import FileUploadParser
from rest_framework import viewsets
from .models import DataDir
from .serializers import DataDirSerializer
import os
from django.conf import settings
from rest_framework.response import Response
from django.core.files.storage import default_storage
from .wcf import WCF

class WavenetViewSet(viewsets.ViewSet):
    def upload(self, request):
        queryset = DataDir.objects.all()
        serializer_class = DataDirSerializer
        file_obj = request.FILES['file']
        file_path = os.path.join(settings.MEDIA_ROOT, 'output.wav')
        file_name = default_storage.save('output.wav', file_obj)
        model = WCF()
        y = model.predict(file_path)
        return Response({'feeling': y})
