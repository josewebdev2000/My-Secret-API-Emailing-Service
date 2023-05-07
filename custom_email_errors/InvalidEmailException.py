# Invalid Email Exception

class InvalidEmailException(Exception):
    """Raise when input was supposed to be an email but is wasn't."""
    
    def __init__(self, failed_email):
        
        self.message = f"{failed_email} is not a valid email."
        super().__init__(self.message)