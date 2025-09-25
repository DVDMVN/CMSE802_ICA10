def filter_edu(emails: list[str]) -> list[str]
    """
    Filters a list of email addresses to keep only those that end in msu.edu

    [save this in edufinder.py]
    """
    filtered_emails = [email for email in emails if email.endswith('msu.edu')]
    return filtered_emails

