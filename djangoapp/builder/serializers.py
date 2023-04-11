# Libraries
from rest_framework import serializers

# Models
from builder.models import Layout


class LayoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Layout
        fields = '__all__'
