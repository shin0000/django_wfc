from rest_framework import serializers
from .models import DataDir

class DataDirSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataDir
        fields = ('upload_path', )