import os
import random
from flask import Flask

app = Flask(__name__)

quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill"
]

@app.route('/')
def get_quote():
    # Pick a random quote from our list
    random_quote = random.choice(quotes)
    return f"<h1>Your Daily Quote:</h1><p><em>{random_quote}</em></p>"
