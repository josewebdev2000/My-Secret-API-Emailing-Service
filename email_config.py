# Configure emails to send for the secret email sending API service

# Make a function to configure the email
# Make a function to send email and detect whether it is plain text or HTML

# Make classes of custom Exceptions to be handled when user input is wrong
import smtplib
from email.message import EmailMessage
from string import Template

from constants import USERNAME, PASSWORD
import helpers

from custom_email_errors.MissingKeyInformationException import MissingKeyInformationException
from custom_email_errors.InvalidEmailException import InvalidEmailException


def make_html_template(html_string = "", sub_vars = {}):
    """Make HTML template to pass to email sending function."""
    
    # Substitute HTML placeholders by their actual values if there is any
    if sub_vars:
        # Make HTML template
        try:
            html_content = Template(html_string)
            html_content = html_content.substitute(sub_vars)
        
        except Exception as e:
            raise e
    
    else:
        html_content = html_string
    
    # return HTML template
    return html_content   
    
def configure_email(sender="", to="", subject="", content="", content_type="plain"):
    """Configure email object."""
    
    # Get any empty kwargs
    empty_kwargs = helpers.get_empty_kwargs(sender=sender, 
                                    to=to, 
                                    subject=subject, 
                                    content=content, 
                                    content_type=content_type)
    
    # If there are empty parameters, raise a MissingKeyInformationException
    if empty_kwargs:
        raise MissingKeyInformationException(empty_kwargs)
    
    # If the given to attribute is not a valid email, raise an InvalidEmailException
    elif not helpers.is_valid_email(to):
        raise InvalidEmailException(to)
    
    # Otherwise, continue with email configuration
    else:
    # Set up headers of email
        email = EmailMessage()
        email["from"] = sender
        email["to"] = to
        email["subject"] = subject
        
        # Set content and its type
        email.set_content(content, content_type)
        
        # Return email object
        return email

def send_email(email_obj):
    """Execute email sending operation."""
    
    # Set google SMPT server to send emails
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as email_server:
        
        # ehlo SMPT to start out communication
        email_server.ehlo()
        
        # Encrypt communication
        email_server.starttls()
        
        # Login with Google Creds
        email_server.login(USERNAME, PASSWORD)
        
        # Send the email
        email_server.send_message(email_obj)