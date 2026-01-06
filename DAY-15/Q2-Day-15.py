# 2) Find all email addresses in text — commented version
import re

text = "Contact: alice@example.com, bob.smith+news@sub.domain.co.in; invalid@com"
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# re.findall returns a list of all non-overlapping matches
emails = re.findall(email_pattern, text)
print("Emails found:", emails)