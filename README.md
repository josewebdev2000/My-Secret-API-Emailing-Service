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

<p>The structure of the JSON object for plain emails and HTML emails without substitution variables is:</p>

<p><code>
{
    "api_key" : "Required API Key to use this service", 
    "sender"  : "name of entity who sends the email",
    "to"      : "email address of the receiver",
    "subject" : "email subject",
    "content" : "email body that contains the main message"
}
</code></p>
</div>
