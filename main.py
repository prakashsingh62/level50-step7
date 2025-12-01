import os
import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

def load_credentials():
    client_secret = os.environ.get("CLIENT_SECRET_JSON")
    token_json = os.environ.get("TOKEN_JSON")

    if not client_secret:
        raise Exception("CLIENT_SECRET_JSON not found in Railway variables")

    if token_json:
        # Load existing token
        creds_data = json.loads(token_json)
        creds = Credentials.from_authorized_user_info(creds_data)
    else:
        raise Exception("TOKEN_JSON missing. Run OAuth flow locally to generate it.")

    return creds


def run_step7():
    creds = load_credentials()

    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()

    # TEST READ
    result = sheet.values().get(
        spreadsheetId="1hKMwlnN3GAE4dxVGvq2WHT2-Om9SJ3P91L8cxioAeoo",
        range="RFQ TEST SHEET!A1"
    ).execute()

    return result
