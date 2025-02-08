import requests
from django.conf import settings

def send_notification_email(to_email, result):
    """Send notification email via Resend API."""
    url = "https://api.resend.com/v1/emails"
    headers = {
        "Authorization": f"Bearer {settings.RESEND_API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "from": "no_reply@gmail.com",
        "to": [to_email],
        "subject": "Evaluation Completed",
        "html": f"<p>Your evaluation is complete. Result: {result}</p>",
    }
    
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses
    except requests.exceptions.RequestException as e:
        print(f"Failed to send email: {e}")
        return None
    
    return response.json()  # Successfully sent email

