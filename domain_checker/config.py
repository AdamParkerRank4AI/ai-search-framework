"""Configuration loader for domain checker credentials.

Reads API keys from environment variables or a .env file.
"""

import os


def load_config() -> dict:
    """Load provider credentials from environment variables.

    Expected env vars:
        GODADDY_API_KEY
        GODADDY_API_SECRET
        NAMECHEAP_API_USER
        NAMECHEAP_API_KEY
        NAMECHEAP_CLIENT_IP
    """
    return {
        "godaddy_key": os.environ.get("GODADDY_API_KEY"),
        "godaddy_secret": os.environ.get("GODADDY_API_SECRET"),
        "namecheap_user": os.environ.get("NAMECHEAP_API_USER"),
        "namecheap_key": os.environ.get("NAMECHEAP_API_KEY"),
        "namecheap_client_ip": os.environ.get("NAMECHEAP_CLIENT_IP"),
    }
