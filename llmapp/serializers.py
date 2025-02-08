from rest_framework import serializers
from .models import EvaluationRequest

class EvaluationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvaluationRequest
        fields = '__all__'
        read_only_fields = ('status', 'result', 'created_at', 'updated_at')
