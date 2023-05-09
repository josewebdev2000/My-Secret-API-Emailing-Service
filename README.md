# My Secret API Email Service

---

<div align="center">
<img src="./email.png" alt="Email Image">
</div>

---

## Overview

<p>This API sends plain text email messages and HTML email messages.</p>
<p>Moreover, This API allows you to send dynamic HTML data through the usage of substitution placeholders.</p>
<p>This API is of private use. However, the source code is free and you can implement it for your own purposes.</p>

## Installation and Execution

1. ### Clone this repository
   
   ```bash
   git clone https://github.com/josewebdev2000/My-Secret-API-Emailing-Service.git
   ```

2. ### Install dependencies
   
   ###### Windows

   ```powershell
      pip install -r requirements.txt
   ```
   ###### Linux/MacOs

   ```bash
      pip3 install -r requirements.txt
   ```

3. ### Set up requried environment variables
   
   ###### Windows

    ```powershell
      set FLASK_APP=server.py
      set FLASK_DEBUG=True
      set API_KEY_FILE="<your_api_key_file>"
      set APP_USERNAME="<your_app_username>"
      set APP_PASSWORD="<your_app_password>"
   ```
   ###### Linux/MacOs

   ```bash
      export FLASK_APP=server.py
      export FLASK_DEBUG=True
      export API_KEY_FILE="<your_api_key_file>"
      export APP_USERNAME="<your_app_username>"
      export APP_PASSWORD="<your_app_password>"
   ```

4. ### Run the API locally on your machine
   
   ###### Windows/Linux/MacOs

   ```powershell
      flask run
   ```

## Explanation

<div>
<h3>API Endpoints</h3>
<p>The two endpoints of my email API service are:</p>
<p>Send plain emails:</p>
<p><code>/send-plain-email</code></p>
<p>Send HTML emails:</p>
<p><code>/send-html-email</code></p>
</div>

<div>
<h3>JSON Data to Send</h3>
<p>These two endpoints receive a <code>JSON</code> object through a <code>POST</code> request</p>

<p>The structure of the JSON object for plain emails and HTML emails without substitution placeholders is:</p>

<p>
<code>{
    "api_key" : "Required API Key to use this service", 
    "sender"  : "name of entity who sends the email",
    "to"      : "email address of the receiver",
    "subject" : "email subject",
    "content" : "email body that contains the main message"
}</code></p>
<p>The structure of the JSON object for HTML emails with substitution placeholders is:</p>
<p><code>{
    "api_key" : "Required API Key to use this service", 
    "sender"  : "name of entity who sends the email",
    "to"      : "email address of the receiver",
    "subject" : "email subject",
    "content" : "email body that contains the main message",
    "sub_vars": {
        "name_var1" : "Value for substitution variable 1",
        "name_var2" : "Value for substitution variable 2"
    }
}</code></p>
</div>

<div>
<h3>JSON object received</h3>
<p>After sending instructions to send email messages. You'll receive a JSON object of the following format:</p>

<p>
<code>{
    "feedback": "feedback message"
}</code></p>

<p>The feedback message will vary depending on whether the message was sent successfully or there was an error.</p>

<div>
<h4>Example Feedback Messages</h4>

<h5>Success Message</h5>
<p>This message is received only when the desired email could be sent.</p>
<code>{
    "feedback": "Your email was sent successfully to {email_address_of_receiver}"
}</code></p>

<h5>Invalid API Message</h5>
<p>This message is received when no API key is specified or when the given API key was incorrect.</p>
<code>{
    "feedback": "Invalid API Key"
}</code></p>

<h5>Missing Key Information Error Message</h5>
<p>This message is received when you forget to specify details such as email subject, email sender, etc.</p>
<code>{
    "feedback": "Cannot send email message without the following information: {information_not_specified}"
}</code></p>

<h5>Invalid Email Message</h5>
<p>This message is received when the email specified in the "to" property is not a valid email.</p>
<code>{
    "feedback": "{invalid_email} is not a valid email."
}</code></p>

<h5>General Email Configuration Error Message</h5>
<p>This message is received when any other error occurred that stopped the configuration of the email to be sent.</p>
<code>{
    "feedback": "Unexpected email configuration error. Make sure you provided the required information to send your email."
}</code></p>

<h5>General Email Sending Error</h5>
<p>This message is received when an error occurred while trying to send the email.</p>
<code>{
    "feedback": "Unexpected email sending error. Try again later."
}</code></p>

<h5>Personal notes on response messages from the API</h5>
<p>It is highly unlikely to receive the last two error messages. However, there may be some scenarios where they could take place.</p>

<p>For instance, you may get the Email Sending Error if your authentication details for the SMTP server you're trying to use fail.</p>

<p>Unfortunately, the last two error messages reveal problems that are hard to debug and would need you to review and change the source code thoroughly.</p>

<p>Fortunately, all the other messages regard the JSON object the API receives. Hence, if there is an error with those, just change the data you're providing in the JSON object until you receive a success message.</p>
</div>

<div>
<h3>Environment Variables</h3>

<p>This project requires the following environment variables to work properly</p>

<h5>API_KEY_FILE</h5>
<p>This environment variable contains the path to the file that the real API Key to test against the one provided by the user.</p>

<h5>APP_USERNAME</h5>
<p>This environment variable refers to the email address used to login to the SMTP server.</p>
<p>All emails will be send from this email address.</p>

<h5>APP_PASSWORD</h5>
<p>This environment variable refers to the password of the email address used to login to the SMTP server.</p>

</div>
</div>

## Clarifications
<div>
<p>The <code>content</code> property of the JSON object is always meant to be a string.</p>
<p>If you're going to send HTML messages. Grab the HTML content as a string and then send it.</p>

<p>I am <strong>NOT</strong> going to share the API key for the service that is on deployment.</p>
<p>The service on deployment uses one of my email addresses to send emails.</p>
<p>However, you may clone this repository and set up your own email and password.</p>
</div>

## Example
<div>
<p>Let's suppose you want to send a reset password page to users of your app.</p>
<p>As always, you want to include the username of the user who forgot his/her password.</p>
<p>In the HTML file, use the following syntax to introduce a substitution placeholder.</p>

```html
<h2>Hello ${username}</h2> 
<p>Click the following link to reset your password <a href="link-to-password-reset">Reset Password</a></p>
```
<p>Then, use the following JSON object to inlcude the username in the HTML email</p>
<p><code>{
    "api_key" : "Required API Key to use this service", 
    "sender"  : "name of entity who sends the email",
    "to"      : "email address of the receiver",
    "subject" : "email subject",
    "content" : "email body that contains the main message",
    "sub_vars": {
        "username" : user_who_forgot_password
    }
}</code></p>

<p>Then the user will receive an email like the following:</p>

```html
<h2>Hello, patrick4523</h2>
<p>Click the following link to reset your password <a href="link-to-password-reset">Reset Password</a></p>
```
</div>
