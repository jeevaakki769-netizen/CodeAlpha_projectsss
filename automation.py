
# CodeAlpha Python Task 3
# Extract Email Addresses from a Text File

import re
from pathlib import Path

input_file = Path("emails.txt")
output_file = Path("extracted_emails.txt")

if not input_file.exists():
    print("Error: emails.txt was not found.")
    print("Create emails.txt and add text containing email addresses.")
else:
    text = input_file.read_text(encoding="utf-8")

    email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    emails = re.findall(email_pattern, text)

    # Remove duplicate email addresses
    unique_emails = list(dict.fromkeys(emails))

    # Save results
    result = "\n".join(unique_emails)
    if not result:
        result = "No email addresses found."

    output_file.write_text(result, encoding="utf-8")

    print(f"Found {len(unique_emails)} unique email address(es).")
    print("Results saved to extracted_emails.txt.")
