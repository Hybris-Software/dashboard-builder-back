from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView

# Serializers
from builder.serializers import LayoutSerializer

# Models
from builder.models import Layout


class Layouts(ListCreateAPIView):
    serializer_class = LayoutSerializer
    queryset = Layout.objects.all()
