import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from dotenv import load_dotenv

load_dotenv()

SCOPES = ['https://mail.google.com/']
TOKEN_PICKLE_FILE = 'token.pickle'

def get_credentials():
    creds = None

    # Check if token.pickle exists and load it
    if os.path.exists(TOKEN_PICKLE_FILE):
        print("✅ Loading OAuth token from token.pickle...")
        with open(TOKEN_PICKLE_FILE, 'rb') as token:
            creds = pickle.load(token)

    # Refresh or re-authenticate if necessary
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("🔄 Refreshing expired OAuth token...")
            creds.refresh(Request())
        else:
            print("🚨 No valid credentials, initiating OAuth login!")

            # Load credentials from environment variables
            client_id = os.getenv('GOOGLE_CLIENT_ID')
            client_secret = os.getenv('GOOGLE_CLIENT_SECRET')

            if not client_id or not client_secret:
                raise Exception("🚨 Google API credentials not found in environment variables.")

            # Set up OAuth flow
            client_config = {
                "installed": {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "redirect_uris": ["urn:ietf:wg:oauth:2.0:oob", "http://localhost"],
                    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                    "token_uri": "https://oauth2.googleapis.com/token"
                }
            }

            flow = InstalledAppFlow.from_client_config(client_config, SCOPES)
            creds = flow.run_local_server(port=0)

        # Save new credentials
        with open(TOKEN_PICKLE_FILE, 'wb') as token:
            pickle.dump(creds, token)
            print("✅ New OAuth token saved!")

    # Print the token for debugging
    if creds:
        print(f"🔑 OAuth Token: {creds.token}")  # Debugging

    return creds