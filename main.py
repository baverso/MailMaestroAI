from libs.google_oauth import get_gmail_credentials
from googleapiclient.discovery import build

def test_gmail():
    """
    Uses the OAuth credentials to build the Gmail API service and lists the user's labels.
    """
    creds = get_gmail_credentials()
    service = build('gmail', 'v1', credentials=creds)
    
    # Call the Gmail API to list the user's labels
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])
    
    if not labels:
        print("No labels found.")
    else:
        print("Labels:")
        for label in labels:
            print(label['name'])

if __name__ == '__main__':
    test_gmail()
