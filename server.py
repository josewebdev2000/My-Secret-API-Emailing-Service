# Flask server to handle POST routes to send plain email text and HTML emails
from flask import Flask, request, jsonify

# Use request.json in order to read JSON data the user sent
