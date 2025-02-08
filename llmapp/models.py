from django.db import models

class EvaluationRequest(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    )
    
    input_data = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    result = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)  # Optional email for notifications
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"EvaluationRequest {self.id} - {self.status}"

