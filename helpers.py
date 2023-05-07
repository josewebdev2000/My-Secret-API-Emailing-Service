# Functions that assist the functionality of the Secret Email Sending API
import re
from constants import EMAIL_REGEX

def get_empty_kwargs(**kwargs):
    """Return keys of empty kwargs."""
    
    return [key for key, value in kwargs.items() if not value]

def is_valid_email(email):
    """Get if an email is valid or not"""
    
    return bool(re.match(EMAIL_REGEX, email))
    