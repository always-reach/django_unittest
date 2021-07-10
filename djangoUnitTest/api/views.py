from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from .models import SampleTable
from .serializer import SampleSerializer


class SampleGet(generics.ListAPIView):
    queryset = SampleTable.objects.all()
    serializer_class = SampleSerializer
