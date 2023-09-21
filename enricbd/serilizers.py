from rest_framework import serializers
from .models import Enric

class EnricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enric
        fields = '__all__'