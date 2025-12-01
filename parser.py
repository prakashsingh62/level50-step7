import json
import os
import gspread
from google.oauth2.service_account import Credentials

def get_sheet():
    """
    Loads Google Sheet using Railway OAuth environment variables.
    """
    client_secret_json = os.environ.get("CLIENT_SECRET_JSON")
    if not client_secret_json:
        raise Exception("CLIENT_SECRET_JSON missing")

    creds_dict = json.loads(client_secret_json)

    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)
    client = gspread.authorize(creds)

    SHEET_ID = "1hKMwlnN3GAE4dxVGvq2WHT2-Om9SJ3P91L8cxioAeoo"
    return client.open_by_key(SHEET_ID)


def parse_sheet_rows(sheet_name="DOMESTIC REGISTER 2025-26"):
    """
    Reads all rows from Level-50 sheet and converts them into a list of dicts.
    """
    sh = get_sheet()
    ws = sh.worksheet(sheet_name)

    rows = ws.get_all_values()

    if not rows or len(rows) < 2:
        return []

    headers = [h.strip() for h in rows[0]]

    data = []
    for i in range(1, len(rows)):
        row_values = rows[i]
        row_dict = {}

        for col_index, col_name in enumerate(headers):
            if col_index < len(row_values):
                row_dict[col_name] = row_values[col_index]
            else:
                row_dict[col_name] = ""

        row_dict["_ROW_NUMBER"] = i + 1  # important for write-back
        data.append(row_dict)

    return data
