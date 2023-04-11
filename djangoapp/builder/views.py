from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

# Serializers
from builder.serializers import LayoutSerializer

# Models
from builder.models import Layout


class Layouts(GenericAPIView):
    serializer_class = LayoutSerializer

    def get_queryset(self):
        return Layout.objects.all()

    def get(self, request):
        queryset = self.get_queryset()
        serializer = LayoutSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LayoutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
