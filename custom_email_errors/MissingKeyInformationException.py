# Missing Key Infomration Exception

class MissingKeyInformationException(Exception):
    """Raise this exception when the user forgets to enter essential information to send the email message."""
    
    def __init__(self, missing_args):
        
        self.message = f"Cannot send email message without the following information: "
        self.message += ", ".join([f"{info}" for info in missing_args])
        self.message += "."
        super().__init__(self.message)