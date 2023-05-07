# Functions that assist the functionality of the Secret Email Sending API

def get_empty_kwargs(**kwargs):
    """Return keys of empty kwargs."""
    
    return [key for key, value in kwargs.items() if not value]
    