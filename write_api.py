import json
import os
import gspread
from google.oauth2.service_account import Credentials

# Columns Level-50 must NOT update
IMMUTABLE = {
    'SALES PERSON', 'CUSTOMER NAME', 'LOCATION', 'RFQ NO', 'RFQ DATE',
    'PRODUCT', 'UID NO', 'UID DATE', 'DUE DATE', 'VENDOR', 'CONCERN PERSON'
}

def safe_write(row, updates):
    """
    Sanitizes update dict by removing forbidden (immutable) columns.
    """
    clean_updates = {}
    for k, v in updates.items():
        if k in IMMUTABLE:
            # skip forbidden fields silently
            continue
        clean_updates[k] = v
    return clean_updates


def get_sheet():
    """
    Loads Google Sheet using Railway environment variables.
    """
    client_secret_json = os.environ.get("CLIENT_SECRET_JSON")
    token_json = os.environ.get("TOKEN_JSON")

    if not client_secret_json:
        raise Exception("CLIENT_SECRET_JSON missing")

    creds_dict = json.loads(client_secret_json)

    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)
    client = gspread.authorize(creds)

    # YOUR SHEET ID (Level-50)
    SHEET_ID = "1hKMwlnN3GAE4dxVGvq2WHT2-Om9SJ3P91L8cxioAeoo"

    return client.open_by_key(SHEET_ID)


def write_to_sheet(row_number, updates):
    """
    Main Level-50 write function used by logic_engine.
    """
    clean_updates = safe_write(row_number, updates)

    sh = get_sheet()
    ws = sh.worksheet("DOMESTIC REGISTER 2025-26")

    # Get header row to map names → column numbers
    headers = ws.row_values(1)
    header_map = {h.strip(): i+1 for i, h in enumerate(headers)}

    for col_name, value in clean_updates.items():
        if col_name in header_map:
            col_index = header_map[col_name]
            ws.update_cell(row_number, col_index, value)

    return True
