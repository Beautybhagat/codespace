pip install Flask
from flask import Flask
import os
import time
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get the full name (Replace 'Your Full Name' with your actual name)
    full_name = "BEAUTY KUMARI BHAGAT"

    # Get the system username
    username = os.getlogin()

    # Get the server time in IST
    server_time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
    
    # Convert server time to IST (UTC +5:30)
    ist_time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time() + 19800))

    # Get top output
    top_output = subprocess.getoutput('top -b -n 1')

    # Create HTML response
    return f"""
    <h1>System Information</h1>
    <p><strong>Name:</strong> {full_name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {ist_time}</p>
    <h2>Top Output</h2>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
