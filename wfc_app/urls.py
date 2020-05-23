from rest_framework.routers import DefaultRouter
from .views import WavenetViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path

# router = DefaultRouter()
wavenet_upload = WavenetViewSet.as_view({'post': 'upload'})
# router.register(r'wavenet', WavenetViewSet)
urlpatterns = format_suffix_patterns([
    path('wavenet_upload/', wavenet_upload, name='wavenet_upload')
])