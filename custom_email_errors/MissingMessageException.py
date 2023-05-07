# Missing Message Exception

# Raise this exception when user tries to send an empty email
class MissingMessageException(Exception):
    """# Raise this exception when user tries to send an empty email."""
    
    def __init__(self):
        self.message = "Cannot send empty email messsge"
        super().__init__(self.message)