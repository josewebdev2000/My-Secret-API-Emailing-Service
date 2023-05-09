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
<p>The two endpoints of my email API service are:</p>
<p>Send plain emails:</p>
<p><code>/send-plain-email</code></p>
<p>Send HTML emails:</p>
<p><code>/send-html-email</code></p>
</div>

<div>
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

## Example
<div>
<p>Let's suppose you want to send a reset password page to users of your app.</p>
<p>As always, you want to include the username of the user who forgot his/her password.</p>
<p>In the HTML file, use the following syntax to introduce a substitution placeholder.</p>
<p>
<code><h2>Hello ${username}</h2> 
<p>Click the following link to reset your password <a href="link-to-password-reset">Reset Password</a></p></code></p>

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
</div>
