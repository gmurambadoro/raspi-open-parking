from rest_framework import viewsets

from .models import Gate, Movement
from .serializers import GateSerializer, MovementSerializer


class GateViewSet(viewsets.ReadOnlyModelViewSet):
    """Provides list and view options for gate configurations"""
    queryset = Gate.objects.all()
    serializer_class = GateSerializer


class MovementViewSet(viewsets.ModelViewSet):
    """Provides list, create, update and delete movements"""
    queryset = Movement.objects.all()
    serializer_class = MovementSerializer
