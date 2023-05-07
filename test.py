import unittest
import helpers

class TestEmailingService(unittest.TestCase):
    
    def setUp(self):
        """Run code before unitests."""
        
        print("About to start unit tests for Email Sending API")
        print("Getting test URLS")
        
        self.plain_email_url, self.html_email_url = helpers.get_urls_from_file()
        print(f"URL for plain emails: {self.plain_email_url}")
        print(f"URL for HTML emails: {self.html_email_url}")
        
        print("Starting unit tests\n\n")
    
    def send_successful_plain_email(self):
        """Test sending a successful plain email."""
        
        print("\nCase 1: Send a successful plain text email")
        
        # Make dict to send as JSON to the API
        email_data = {
            
        }