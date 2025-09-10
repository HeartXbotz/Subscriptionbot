import datetime

def format_expiry(expiry):
    if not expiry:
        return "N/A"
    return expiry.strftime("%Y-%m-%d %H:%M")
