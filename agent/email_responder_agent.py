# agent/email_responder_agent.py

from googleapiclient.discovery import build
from libs.google_oauth import get_gmail_credentials

# Import stub functions from tools.
from tools.email_categorizer import categorize_email
from tools.answer_email import answer_email
from tools.archive_email import archive_email
# (Import other tools as needed later.)

def get_new_emails(service):
    """
    Retrieve new emails from the user's INBOX.
    """
    results = service.users().messages().list(userId='me', labelIds=['INBOX']).execute()
    messages = results.get('messages', [])
    return messages

def process_email(message_id, service):
    """
    Process a single email: analyze, categorize, decide the appropriate action,
    and trigger the corresponding tool. Includes interactive prompts.
    """
    # Retrieve the full email message.
    message = service.users().messages().get(userId='me', id=message_id, format='full').execute()
    snippet = message.get('snippet', '')
    print(f"\nProcessing email {message_id}:")
    print(snippet)
    
    # Extract the threadId from the message.
    # Every email should have a threadId field.
    thread_id = message.get('threadId', None)
    if not thread_id:
        # Fallback: if threadId is missing, use message_id (not typical)
        thread_id = message_id
    print(f"Extracted thread ID: {thread_id}")
    
    # Categorize the email using the Email Categorizer tool.
    category = categorize_email(message)
    print("Email category:", category)
    
    # Ask for human approval before proceeding with actions.
    user_input = input("Approve this email for processing? (y/n): ").strip().lower()
    if user_input != 'y':
        print("Skipping email based on user input.")
        return

    # Decision logic based on the category.
    if category == "warm-up":
        # For warm-up emails, archive without further action.
        archive_email(thread_id, service)
    elif category == "needs_response":
        # Generate an answer using the Answer Email tool.
        response = answer_email(message)
        print("Generated response:", response)
        send_input = input("Send the generated response? (y/n): ").strip().lower()
        if send_input == 'y':
            # Here, you would call your send_gmail_email tool.
            print("Response would be sent (stub).")
        else:
            print("Response not sent based on user input.")
        archive_email(thread_id, service)
    elif category == "meeting_request":
        meeting_input = input("Proceed with booking a meeting? (y/n): ").strip().lower()
        if meeting_input == 'y':
            print("Booking meeting (tool stub).")
            # Call the meeting booking tool here.
        else:
            print("Skipping meeting booking.")
        archive_email(thread_id, service)
    else:
        print("No specific action chosen; archiving the email.")
        archive_email(thread_id, service)


#def process_email(message_id, service):
    """
    Process a single email: analyze, categorize, decide the appropriate action,
    and trigger the corresponding tool. It now includes interactive prompts for human approval.
    """
    # Retrieve the full email message.
    message = service.users().messages().get(userId='me', id=message_id, format='full').execute()
    snippet = message.get('snippet', '')
    print(f"\nProcessing email {message_id}:")
    print(snippet)
    
    # Extract the threadId from the message.
    thread_id = message.get('threadId', message_id)
    
    # Categorize the email using the Email Categorizer tool.
    category = categorize_email(message)
    print("Email category:", category)
    
    # Ask for human approval before proceeding with actions.
    user_input = input("Approve this email for processing? (y/n): ").strip().lower()
    if user_input != 'y':
        print("Skipping email based on user input.")
        return

    # Decision logic based on the category.
    if category == "warm-up":
        # For warm-up emails, archive without further action.
        archive_email(thread_id, service)
    elif category == "needs_response":
        # Generate an answer using the Answer Email tool.
        response = answer_email(message)
        print("Generated response:", response)
        send_input = input("Send the generated response? (y/n): ").strip().lower()
        if send_input == 'y':
            # For example, call your send_gmail_email tool here.
            print("Response would be sent (stub).")
        else:
            print("Response not sent based on user input.")
        archive_email(thread_id, service)
    elif category == "meeting_request":
        meeting_input = input("Proceed with booking a meeting? (y/n): ").strip().lower()
        if meeting_input == 'y':
            print("Booking meeting (tool stub).")
            # Call check_calendar/book meeting tool here.
        else:
            print("Skipping meeting booking.")
        archive_email(thread_id, service)
    else:
        print("No specific action chosen; archiving the email.")
        archive_email(thread_id, service)


#def process_email(message_id, service):
    """
    Process a single email: analyze, categorize, decide the appropriate action,
    and trigger the corresponding tool. It now includes interactive prompts for human approval.
    """
    # Retrieve the full email message.
    message = service.users().messages().get(userId='me', id=message_id, format='full').execute()
    snippet = message.get('snippet', '')
    print(f"\nProcessing email {message_id}:")
    print(snippet)
    
    # Categorize the email using the Email Categorizer tool.
    category = categorize_email(message)
    print("Email category:", category)
    
    # Ask for human approval before proceeding with actions.
    user_input = input("Approve this email for processing? (y/n): ").strip().lower()
    if user_input != 'y':
        print("Skipping email based on user input.")
        return

    # Decision logic based on the category.
    if category == "warm-up":
        # For warm-up emails, archive without further action.
        archive_email(message_id, service)
    elif category == "needs_response":
        # Generate an answer using the Answer Email tool.
        response = answer_email(message)
        print("Generated response:", response)
        # Here, you might include another prompt for sending the response.
        send_input = input("Send the generated response? (y/n): ").strip().lower()
        if send_input == 'y':
            # For example, call your send_gmail_email tool here.
            # send_gmail_email(message_id, response, service)
            print("Response would be sent (stub).")
        else:
            print("Response not sent based on user input.")
        archive_email(message_id, service)
    elif category == "meeting_request":
        # Meeting requests: prompt for approval of scheduling.
        meeting_input = input("Proceed with booking a meeting? (y/n): ").strip().lower()
        if meeting_input == 'y':
            print("Booking meeting (tool stub).")
            # Here you would call your check_calendar or book_meeting tool.
        else:
            print("Skipping meeting booking.")
        archive_email(message_id, service)
    else:
        # Default: archive the email.
        print("No specific action chosen; archiving the email.")
        archive_email(message_id, service)


#def process_email(message_id, service):
#    """
#    Process a single email: analyze, categorize, decide the appropriate action,
#    and trigger the corresponding tool.
#    """
#    # Retrieve the full email message.
#    message = service.users().messages().get(userId='me', id=message_id, format='full').execute()
#    snippet = message.get('snippet', '')
#    print(f"Processing email {message_id}: {snippet}")
#
#    # Categorize the email using the Email Categorizer tool.
#    category = categorize_email(message)
#    print("Email category:", category)
#    
#    # Decision logic based on the category.
#    if category == "warm-up":
#        # For warm-up emails, archive without further action.
#        archive_email(message_id, service)
#    elif category == "needs_response":
#        # Generate an answer using the Answer Email tool.
#        response = answer_email(message)
#        print("Generated response:", response)
#        # Here, you might also use send_gmail_email to send the response.
#        archive_email(message_id, service)
#    elif category == "meeting_request":
#        # Call the Check Calendar / Book Meeting tool (to be implemented).
#        print("Meeting request detected: booking a meeting (tool stub).")
#        # For now, archive after processing.
#        archive_email(message_id, service)
#    else:
#        # Default: archive the email.
#        print("No action needed, archiving the email.")
#        archive_email(message_id, service)

def run_agent():
    """
    Main function to run the Email Responder Agent.
    """
    creds = get_gmail_credentials()
    service = build('gmail', 'v1', credentials=creds)
    
    # Retrieve new emails.
    messages = get_new_emails(service)
    print(f"Found {len(messages)} new emails.")
    
    # Process each email.
    for msg in messages:
        process_email(msg['id'], service)

if __name__ == '__main__':
    run_agent()
