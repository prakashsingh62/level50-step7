from datetime import datetime, timedelta

def classify(row):
    cp=row.get('CONCERN PERSON','').strip().upper()
    if cp=='NP': return {'section':'Skip','action':'No action (NP)'}
    due=datetime.strptime(row['DUE DATE'],'%Y-%m-%d')
    today=datetime.now()+timedelta(hours=5,minutes=30)
    days_left=(due.date()-today.date()).days
    if row.get('VENDOR RESPONSE RECEIVED','').lower() in ('yes','y'):
        return {'section':'Quotation Received','action':'No reminder'}
    if days_left<0: return {'section':'Overdue','action':'Overdue — escalate'}
    if days_left<=2: return {'section':'High','action':'Urgent reminder'}
    if days_left<=3: return {'section':'Medium','action':'Reminder'}
    if days_left<=4: return {'section':'Low','action':'Monitor'}
    return {'section':'Low','action':'No action'}
