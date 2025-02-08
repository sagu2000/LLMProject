from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import EvaluationRequest
from .serializers import EvaluationRequestSerializer
from rest_framework.generics import RetrieveAPIView
from .tasks import process_evaluation_request

class EvaluationRequestCreateView(APIView):
    def post(self, request):
        serializer = EvaluationRequestSerializer(data=request.data)
        if serializer.is_valid():
            evaluation_request = serializer.save(status="pending")
            process_evaluation_request.delay(evaluation_request.id)  # Trigger Celery task
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EvaluationRequestDetailView(RetrieveAPIView):
    # Retrieve details of an evaluation request by ID
    queryset = EvaluationRequest.objects.all()
    serializer_class = EvaluationRequestSerializer

