from rest_framework import serializers

from .models import SampleTable


class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleTable
        fields = ("name", "phone")
