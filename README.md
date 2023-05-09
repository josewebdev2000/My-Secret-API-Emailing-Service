# My Secret API Email Service

---

<div align="center">
<img src="./email.png" alt="Email Image">
</div>

---

## Overview

<p>This API sends plain text email messages and HTML email messages.</p>
<p>Moreover, This API allows you to send dynamic HTML data through the usage of substitution placeholders</p>
<p>This API is of private use. However, the source code is free and you can implement it for your own purposes.</p>

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

<h2>Hello, patrick4523</h2>
<p>Click the following link to reset your password <a href="link-to-password-reset">Reset Password</a></p>

</div>
