# tools/email_categorizer.py

def categorize_email(message):
    """
    Analyze the email message and return a category string.
    For now, this is a stub that categorizes based on simple criteria.
    
    Example categories:
    - "warm-up"
    - "needs_response"
    - "meeting_request"
    - "other"
    """
    snippet = message.get('snippet', '').lower()
    
    if "warmup" in snippet:
        return "warm-up"
    elif "meeting" in snippet:
        return "meeting_request"
    elif "unsubscribe" in snippet or "newsletter" in snippet:
        return "needs_response"
    else:
        # Default for this stub.
        return "needs_response"
