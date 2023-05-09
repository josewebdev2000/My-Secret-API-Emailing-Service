# Global constants to be used throughout the Secret Email API Sending Project

# import os to get environ vars
import os

API_KEY_FILE = os.environ["API_KEY_FILE"]
USERNAME = os.environ["APP_USERNAME"]
PASSWORD = os.environ["APP_PASSWORD"]
EMAIL_REGEX = r"^[\w\.-]+@[\w\.-]+\.\w+$"
REQUIRED_INFO = ("sender", "to", "subject", "content", "message_type")