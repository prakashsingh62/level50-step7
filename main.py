import gspread
from oauth2client.service_account import ServiceAccountCredentials
from parser import clean
from logic_engine import classify
from templates import build_email
from write_api import safe_write
from email_sender import send_email

TEST_SHEET_ID='1hKMwlnN3GAE4dxVGvq2WHT2-Om9SJ3P91L8cxioAeoo'
TAB_NAME='RFQ TEST SHEET'
SENDER='sales@ventilengineering.com'
TEST_RECIPIENT='sales@ventilengineering.com'

def run_step7():
    creds=ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',["https://www.googleapis.com/auth/spreadsheets"])
    gc=gspread.authorize(creds)
    ws=gc.open_by_key(TEST_SHEET_ID).worksheet(TAB_NAME)
    rows=ws.get_all_records()
    for i,row in enumerate(rows,start=2):
        r=clean(row)
        result=classify(r)
        subject,body=build_email(result['section'],result['action'],r)
        send_email(SENDER,TEST_RECIPIENT,subject,body)
        updates={'LAST ACTION':result['action']}
        col=ws.find('LAST ACTION').col
        ws.update_cell(i,col,updates['LAST ACTION'])
    return 'Step-7 Test Completed'

if __name__=='__main__':
    print(run_step7())
