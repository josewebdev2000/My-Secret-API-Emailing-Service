import unittest
import helpers
from pathlib import Path

class TestEmailingService(unittest.TestCase):
    
    def setUp(self):
        """Run code before unitests."""
        
        print("About to start unit tests for Email Sending API")
        print("Getting test URLS")
        
        self.api_key = "adbpqBr3jLfe3FAJyeoO581MueEwPaUHm3bCYXwz6YjXAOMZ7St8IYAUsLWj"
        
        self.plain_email_url, self.html_email_url = helpers.get_urls_from_file("email_urls.txt")
        print(f"URL for plain emails: {self.plain_email_url}")
        print(f"URL for HTML emails: {self.html_email_url}")
        
        print("Starting unit tests\n\n")
    
    def test_send_successful_plain_email(self):
        """Test sending a successful plain email."""
        
        print("\nCase 1: Send a successful plain text email")
        
        # Make dict to send as JSON to the API
        email_data = {
            "api_key": self.api_key,
            "sender" : "JBG",
            "to": "jabg1234@protonmail.com",
            "subject": "Sending plain text over email",
            "content": "Example of how to send plain text over email",
        }
        
        # Give instructions to send the email
        server_res = helpers.send_json_to_url(email_data, self.plain_email_url)
        
        # Read the JSON response as a dict
        response_dict = helpers.read_res_from_url(server_res)
        
        # Make variables for received response and expected response
        actual_message = response_dict.get("message")
        expected_message = f"Your email was sent successfully to {email_data.get('to')}"
        
        # Assert both the actual message and the expected message are equal
        self.assertEqual(actual_message, expected_message)
    
    def test_sending_plain_email_without_api_key(self):
        """Try sending out a plain email without providing an API Key."""
        
        print("\nCase 2: Try to send plain email without API Key")
        
        # Make dict to send as JSON to the API
        email_data = {
            "sender" : "JBG",
            "to": "jabg1234@protonmail.com",
            "subject": "Sending plain text over email",
            "content": "Example of how to send plain text over email",
        }
        
        # Give instructions to send the email
        server_res = helpers.send_json_to_url(email_data, self.plain_email_url)
        
        # Read the JSON response as a dict
        response_dict = helpers.read_res_from_url(server_res)
        
        # Make variables for received response and expected response
        actual_message = response_dict.get("message")
        expected_message = "Invalid API Key"
        
        # Assert both the actual message and the expected message are equal
        self.assertEqual(actual_message, expected_message)
    
    def test_raise_missing_key_information_exception(self):
        """Try raising the missing key information exception for the plain email."""
        
        print("\nCase 3: Raise Exception from trying to send email without key information")
        
        # Make dict to send as JSON to the API
        email_data = {
            "api_key": self.api_key,
            "sender" : "JBG",
            "to": "jabg1234@protonmail.com",
            "subject": "I am you",
            "content": ""
        }
        
        # Give instructions to send the email
        server_res = helpers.send_json_to_url(email_data, self.plain_email_url)
        
        # Read the JSON response as a dict
        response_dict = helpers.read_res_from_url(server_res)
        
        # Make variables for received response and expected response
        actual_message = response_dict.get("message")
        expected_message = "Cannot send email message without the following information: content."
        
        # Assert both the actual message and the expected message are equal
        self.assertEqual(actual_message, expected_message)
    
    def test_raise_invalid_email_exception(self):
        """Try raising the invalid email exception for the plain email."""
        
        print("\nCase 4: Raise Exception from trying to send an email without a receiver")
        
        # Make dict to send as JSON to the API
        email_data = {
            "api_key": self.api_key,
            "sender" : "JBG",
            "to": "lalarinlinla",
            "subject": "I am you",
            "content": "Just accept it. I am you my man"
        }
        
        # Give instructions to send the email
        server_res = helpers.send_json_to_url(email_data, self.plain_email_url)
        
        # Read the JSON response as a dict
        response_dict = helpers.read_res_from_url(server_res)
        
        # Make variables for received response and expected response
        actual_message = response_dict.get("message")
        expected_message = f"{email_data.get('to')} is not a valid email."
        
        # Assert both the actual message and the expected message are equal
        self.assertEqual(actual_message, expected_message)
    
    def test_send_successful_html_email_no_placeholders(self):
        """Confirm it's possible to send successful HTML messages without placeholders."""
        
        print("\nCase 5: Successfully send HTML email without placeholders")
        
        # Get html string
        html_string = Path("html_for_testing", "no_template.html").read_text()
        
        # Make dict to send as JSON to the API
        email_data = {
            "api_key": self.api_key,
            "sender" : "JBG",
            "to": "jabg1234@protonmail.com",
            "subject": "Sending HTML Data no placeholders",
            "content": html_string
        }
        
        # Give instructions to send the email
        server_res = helpers.send_json_to_url(email_data, self.html_email_url)
        
        # Read the JSON response as a dict
        response_dict = helpers.read_res_from_url(server_res)
        
        # Make variables for received response and expected response
        actual_message = response_dict.get("message")
        expected_message = f"Your email was sent successfully to {email_data.get('to')}"
        
        # Assert both the actual message and the expected message are equal
        self.assertEqual(actual_message, expected_message)
    
    def test_send_successful_html_email_with_placeholders(self):
        """Successfully send an HTML email with placeholders."""
        
        print("\nCase 6: Successfully send HTML email with placeholders")
        
        # Get html string
        html_string = Path("html_for_testing", "template.html").read_text()
        
        # Make dict to send as JSON to the API
        email_data = {
            "api_key": self.api_key,
            "sender" : "JBG",
            "to": "jabg1234@protonmail.com",
            "subject": "Sending HTML Data with placeholders",
            "content": html_string,
            "sub_vars": {
                "name": "Antonio Valderrama",
                "age": "31",
                "country": "Chile",
                "occupation": "Industrial Designer"
            }
        }
        
        # Give instructions to send the email
        server_res = helpers.send_json_to_url(email_data, self.html_email_url)
        
        # Read the JSON response as a dict
        response_dict = helpers.read_res_from_url(server_res)
        
        # Make variables for received response and expected response
        actual_message = response_dict.get("message")
        expected_message = f"Your email was sent successfully to {email_data.get('to')}"
        
        # Assert both the actual message and the expected message are equal
        self.assertEqual(actual_message, expected_message)
    
    def test_miss_placeholders_send_html_email(self):
        """Raise an Exception when the user does not enter the proper placeholders"""
        
        print("\nCase 7: Successfully send HTML email with placeholders")
        
        # Get html string
        html_string = Path("html_for_testing", "template.html").read_text()
        
        # Make dict to send as JSON to the API
        email_data = {
            "api_key": self.api_key,
            "sender" : "JBG",
            "to": "jabg1234@protonmail.com",
            "subject": "Sending HTML Data with placeholders",
            "content": html_string,
            "sub_vars": {
                "name": "Antonio Sarazosa",
                "ae": "31",
                "county": "Chile",
                "occupation": "Industrial Designer"
            }
        }
        
        # Give instructions to send the email
        server_res = helpers.send_json_to_url(email_data, self.html_email_url)
        
        # Read the JSON response as a dict
        response_dict = helpers.read_res_from_url(server_res)
        
        # Make variables for received response and expected response
        actual_message = response_dict.get("message")
        expected_message = "Mispelling error in JSON given placeholder: 'age'"
        
        # Assert both the actual message and the expected message are equal
        self.assertEqual(actual_message, expected_message)
    
    def test_send_successful_html_email_no_api_key(self):
        """Try sending an HTML email without API Key."""
        
        print("\nCase 8: Successfully send HTML email without placeholders")
        
        # Get html string
        html_string = Path("html_for_testing", "no_template.html").read_text()
        
        # Make dict to send as JSON to the API
        email_data = {
            "sender" : "JBG",
            "to": "jabg1234@protonmail.com",
            "subject": "Sending HTML Data no placeholders",
            "content": html_string
        }
        
        # Give instructions to send the email
        server_res = helpers.send_json_to_url(email_data, self.html_email_url)
        
        # Read the JSON response as a dict
        response_dict = helpers.read_res_from_url(server_res)
        
        # Make variables for received response and expected response
        actual_message = response_dict.get("message")
        expected_message = "Invalid API Key"
        
        # Assert both the actual message and the expected message are equal
        self.assertEqual(actual_message, expected_message)

if __name__ == "__main__":
    unittest.main()