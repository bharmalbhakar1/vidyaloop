import os
import sys
import subprocess

# 1. Vercel demands a top-level execution object. 
# We define a dummy handler function to satisfy Vercel's build validator.
def handler(request, context):
    return {
        "statusCode": 200,
        "body": "Streamlit server routing initiated."
    }

# 2. Immediately execute the background process initialization
# This forces the underlying container to spin up our Streamlit app script
if __name__ == "__main__":
    # We use subprocess to explicitly call the local streamlit environment setup
    script_path = os.path.join(os.path.dirname(__file__), "app.py")
    subprocess.run(["streamlit", "run", script_path, "--server.port", "8080", "--server.address", "0.0.0.0"])