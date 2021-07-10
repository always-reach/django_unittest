from django.urls import path

from .views import SampleGet

urlpatterns = [
    path(r'sampleget', SampleGet.as_view(), name='detail'),
]
