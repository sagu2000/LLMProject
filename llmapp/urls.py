from django.urls import path
from .views import EvaluationRequestCreateView, EvaluationRequestDetailView

urlpatterns = [
    path('evaluation-requests/', EvaluationRequestCreateView.as_view(), name='create-evaluation-request'),
    path('evaluation-requests/<int:pk>/', EvaluationRequestDetailView.as_view(), name='evaluation-request-detail'),
]
