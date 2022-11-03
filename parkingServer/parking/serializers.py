from rest_framework import serializers

from .models import Gate, Movement


class GateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gate
        fields = '__all__'


class MovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movement
        fields = '__all__'

