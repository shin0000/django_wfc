from django.db import models

class DataDir(models.Model):
    upload_path = models.FileField(upload_to='uploads/%Y/%m/%d/')
    
    def __str__(self):
        return self.upload_path
