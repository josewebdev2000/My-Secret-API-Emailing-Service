# Configure emails to send for the secret email sending API service

# Make a function to configure the email
# Make a function to send email and detect whether it is plain text or HTML

# Make classes of custom Exceptions to be handled when user input is wrong
import smtplib
from email.message import EmailMessage
from string import Template

from constants import USERNAME, PASSWORD
from helpers import get_empty_kwargs

from custom_email_errors.MissingKeyInformationException import MissingKeyInformationException
from custom_email_errors.MissingMessageException import MissingMessageException

def make_html_template(html_string = "", sub_vars = {}):
    """Make HTML template to pass to email sending function."""
    
    # Continue only if an html_string was provided
    if html_string:
        
        # Make HTML template
        html_content = Template(html_string)
        
        # Substitute HTML placeholders by their actual values if there is any
        if sub_vars:
            html_content = html_content.substitute(sub_vars)
        
        # return HTML template
        return html_content  
    
    # Otherwise, raise a MissingMessageException
    else:
        raise MissingMessageException()     
    
def configure_email(sender="", to="", subject="", content="", content_type="plain"):
    """Configure email object."""
    
    # Get any empty kwargs
    empty_kwargs = get_empty_kwargs(sender=sender, 
                                    to=to, 
                                    subject=subject, 
                                    content=content, 
                                    content_type=content_type)
    
    # If there are not empty parameters, continue
    if not empty_kwargs:
    
        # Set up headers of email
        email = EmailMessage()
        email["from"] = sender
        email["to"] = to
        email["subject"] = subject
        
        # Set content and its type
        email.set_content(content, content_type)
        
        # Return email object
        return email
    
    # Otherwise, raise a MissingKeyInformationException
    else:
        raise MissingKeyInformationException(empty_kwargs)

def send_email(email_obj):
    """Execute email sending operation."""
    
    # Set google SMPT server to send emails
    with smtplib.SMTP(host="smpt.gmail.com", port=587) as email_server:
        
        # ehlo SMPT to start out communication
        email_server.ehlo()
        
        # Encrypt communication
        email_server.starttls()
        
        # Login with Google Creds
        email_server.login(USERNAME, PASSWORD)
        
        # Send the email
        email_server.send_message(email_obj)