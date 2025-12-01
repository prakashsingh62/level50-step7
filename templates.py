def build_email(section, action, row):
    subject=f"[TEST MODE] {section} — RFQ {row['RFQ NO']}"
    body=(
        f"RFQ No: {row['RFQ NO']}\n"
        f"Customer: {row['CUSTOMER NAME']}\n"
        f"Vendor: {row['VENDOR']}\n"
        f"Due Date: {row['DUE DATE']}\n\n"
        f"Section: {section}\n"
        f"Action: {action}\n\n"
        "-- Level-50 Test Mode"
    )
    return subject, body
