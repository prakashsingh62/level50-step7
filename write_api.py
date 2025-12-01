IMMUTABLE={'SALES PERSON','CUSTOMER NAME','LOCATION','RFQ NO','RFQ DATE','PRODUCT','UID NO','UID DATE','DUE DATE','VENDOR','CONCERN PERSON'}

def safe_write(row, updates):
    for k in updates:
        if k in IMMUTABLE:
            raise Exception(f'Attempted write to immutable column: {k}')
    return updates
