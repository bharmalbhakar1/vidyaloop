import os
import sys

# Route execution requests straight into the Streamlit rendering engine
from streamlit.web import cli as stcli

if __name__ == "__main__":
    sys.argv = ["streamlit", "run", "app.py", "--server.port", "8080", "--server.address", "0.0.0.0"]
    sys.exit(stcli.main())