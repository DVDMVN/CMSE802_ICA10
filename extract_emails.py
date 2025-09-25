import re

def extract_emails(html: str) -> list[str]:
    email_regex = re.compile(r"[\w\-\.]+@(?:[\w-]+\.)+[\w-]{2,}")
    emails = re.findall(email_regex, html)
    return emails