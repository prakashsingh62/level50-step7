from logic_engine import run_step7
from write_api import write_to_sheet
from email_sender import send_email
from parser import parse_sheet_rows
from templates import build_email_template

def main():
    try:
        print("🔁 Running Level-50 Step-7 Test on Railway…")

        # 1. Process sheet data
        rows = parse_sheet_rows()
        print(f"📄 Parsed {len(rows)} rows")

        # 2. Run logic engine
        results = run_step7(rows)
        print("⚙ Logic engine completed")

        # 3. Build email content
        email_body = build_email_template(results)
        print("✉ Email template generated")

        # 4. Send email via OAuth Gmail
        send_email(
            to="sales@ventilengineering.com",
            subject="Level-50 Step-7 Test Run",
            body=email_body
        )
        print("📨 Email sent successfully")

        # 5. Write back to Google Sheet
        write_to_sheet(results)
        print("📊 Sheet updated")

        return {"status": "success", "message": "Step-7 completed"}

    except Exception as e:
        print("❌ ERROR:", str(e))
        return {"status": "error", "message": str(e)}


if __name__ == "__main__":
    main()
