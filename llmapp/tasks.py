
import time
from celery import shared_task
from .models import EvaluationRequest
from .utils import send_notification_email

@shared_task
def process_evaluation_request(request_id):
    # Process the evaluation request and send an email
    try:
        evaluation = EvaluationRequest.objects.get(id=request_id)
        evaluation.status = "processing"
        evaluation.save()
        time.sleep(5)  # we can add real evaluation logic
        
        # Updating result
        evaluation.result = f"Processed result for: {evaluation.input_data}"
        evaluation.status = "completed"
        evaluation.save()

        # Send notification email
        if evaluation.email:
            send_notification_email(evaluation.email, evaluation.result)
        return "Task completed"
    except EvaluationRequest.DoesNotExist:
        return "Request not found"
