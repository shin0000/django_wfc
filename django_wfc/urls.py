from django.contrib import admin
from django.urls import path, include
# from wfc_app.urls import router as r1


urlpatterns = [
    path('admin/', admin.site.urls),
    path('wfc_app/', include('wfc_app.urls')),
]
