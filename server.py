# Flask server to handle POST routes to send plain email text and HTML emails
from flask import Flask, request, render_template, jsonify

import email_config

from custom_email_errors.MissingKeyInformationException import MissingKeyInformationException
from custom_email_errors.InvalidEmailException import InvalidEmailException

from constants import API_KEY_FILE

# Make an instance of the app
app = Flask(__name__)

# Make a route to explain what this app is about
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# Make a route to send plain emails
@app.route("/send-plain-email", methods=["POST"])
def send_plain_email():
    
    # Use request.json in order to read JSON data the user sent
    email_info = request.json
    
    # Create a response dict to send as JSON to let the user know how it all went
    feedback = {"message": ""}
    
    # Grab the API Key given by the user
    email_api_key = email_info.get("api_key", "")
    
    # Grab the real API Key
    with open(API_KEY_FILE) as api_file:
        real_api_key = api_file.read()
    
    # If the real apy key is not equal to the given API, send invalid API message and cancel all operations
    if real_api_key != email_api_key:
        feedback["message"] = "Invalid API Key"
    
    # Since the API Key is correct. Continue as usual
    else:
    
        # Unpack required information to send email
        email_sender = email_info.get("sender", "")
        email_to = email_info.get("to", "")
        email_subject = email_info.get("subject", "")
        email_content = email_info.get("content", "")
        
        # Configure the email to send
        try:
            email_to_send_obj = email_config.configure_email(sender = email_sender,
                                                            to = email_to,
                                                            subject = email_subject,
                                                            content = email_content)   
        except MissingKeyInformationException as e:
            feedback["message"] = e.message
        
        except InvalidEmailException as e:
            feedback["message"] = e.message
        
        except Exception:
            feedback["message"] = "Unexpected email configuration error. Make sure you provided the required information to send your email."
            
        # If the previous was successful, please send the email
        else:
            try:
                email_config.send_email(email_to_send_obj)
            
            except Exception:
                feedback["message"] = "Unexpected email sending error. Try again later."
            
            else:
                feedback["message"] = f"Your email was sent successfully to {email_to}"
    
    return jsonify(feedback)

@app.route("/send-html-email", methods=["POST"])
def send_html_email():
    
    # Use request.json in order to read JSON data the user sent
    email_info = request.json
    
    # Create a response dict to send as JSON to let the user know how it all went
    feedback = {"message": ""}
    
    # Grab the API Key given by the user
    email_api_key = email_info.get("api_key", "")
    
    # Grab the real API Key
    with open(API_KEY_FILE) as api_file:
        real_api_key = api_file.read()
    
    # If the api key the user entered is not equal to the real API, send Invalid API Key message
    if email_api_key != real_api_key:
        feedback["message"] = "Invalid API Key"
    
    else:
    
        # Unpack required information to send email
        email_sender = email_info.get("sender", "")
        email_to = email_info.get("to", "")
        email_subject = email_info.get("subject", "")
        email_sub_vars = email_info.get("sub_vars", {})
        
        try:
            email_content = email_config.make_html_template(html_string = email_info.get("content", ""), sub_vars=email_sub_vars)
        
        except KeyError as e:
            feedback["message"] = f"Mispelling error in JSON given placeholder: {e}"
        
        else:
            email_message_type = "html"
            
            # Configure the email to send
            try:
                email_to_send_obj = email_config.configure_email(sender = email_sender,
                                                                to = email_to,
                                                                subject = email_subject,
                                                                content = email_content,
                                                                content_type = email_message_type)   
            except MissingKeyInformationException as e:
                feedback["message"] = e.message
            
            except InvalidEmailException as e:
                feedback["message"] = e.message
            
            except Exception as e:
                feedback["message"] = "Unexpected email configuration error. Make sure you provided the required information to send your email."
                
            # If the previous was successful, please send the email
            else:
                try:
                    email_config.send_email(email_to_send_obj)
                
                except Exception:
                    feedback["message"] = "Unexpected email sending error. Try again later."
                
                else:
                    feedback["message"] = f"Your email was sent successfully to {email_to}"
    
    return jsonify(feedback)
