import base64
from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES=[
    'https://www.googleapis.com/auth/gmail.send',
    'https://www.googleapis.com/auth/gmail.compose',
    'https://www.googleapis.com/auth/gmail.modify'
]

def get_service():
    creds=Credentials.from_authorized_user_file('token.json',SCOPES)
    return build('gmail','v1',credentials=creds)

def create_message(sender,to,subject,body):
    msg=MIMEText(body)
    msg['to']=to; msg['from']=sender; msg['subject']=subject
    raw=base64.urlsafe_b64encode(msg.as_bytes()).decode()
    return {'raw':raw}

def send_email(sender,to,subject,body):
    service=get_service()
    service.users().messages().send(userId='me',body=create_message(sender,to,subject,body)).execute()
    return True
