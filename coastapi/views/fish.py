from rest_framework import serializers
from coastapi.models import Fish
from .fishtype import FishTypeSerializer

class FishSerializer(serializers.ModelSerializer):
    fish_type = FishTypeSerializer(many=False)

    class Meta:
        model = Fish
        fields = '__all__'