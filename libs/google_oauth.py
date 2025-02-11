import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Define the required OAuth scopes. For modifying Gmail (e.g., archiving), we need gmail.modify.
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def get_gmail_credentials():
    """
    Authenticates with the Gmail API using OAuth and returns valid credentials.
    It uses a token.pickle file to store/reuse access tokens.
    """
    creds = None
    token_file = os.path.join(os.path.dirname(__file__), '..', 'token.pickle')
    # Path to your credentials file located in the config folder
    credentials_file = os.path.join(os.path.dirname(__file__), '..', 'config', 'credentials.json')
    
    # Check if the token file exists and load the credentials
    if os.path.exists(token_file):
        with open(token_file, 'rb') as token:
            creds = pickle.load(token)
    
    # If no valid credentials, initiate the OAuth flow
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_file, SCOPES)
            # Use a fixed port to have a consistent redirect URI (ensure it's authorized in your Google Console)
            creds = flow.run_local_server(port=8080)
        # Save the new credentials for future runs
        with open(token_file, 'wb') as token:
            pickle.dump(creds, token)
    
    return creds
