# tools/archive_email.py

def archive_email(thread_id, service):
    """
    Archive the email by removing the INBOX label.
    """
    body = {"removeLabelIds": ["INBOX"]}
    try:
        print(f"Attempting to archive thread with ID: {thread_id}")
        #service.users().threads().modify(userId='me', threadId=message_id, body=body).execute()
        #service.users().threads().modify(userId='me', id=message_id, body=body).execute()
        service.users().threads().modify(userId='me', id=thread_id, body=body).execute()
        print(f"Archived email/thread {thread_id}.")
    except Exception as e:
        print(f"Failed to archive email {thread_id}: {e}")
