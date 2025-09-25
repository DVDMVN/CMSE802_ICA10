# combine.py

def combine_handles(emails: list[str]) -> str:

    handles = []
    for email in emails:
        if "@" in email:
            parts = email.split("@")
            handle = parts[0]
            handles.append(handle)

    result = ",".join(handles)

    return result
