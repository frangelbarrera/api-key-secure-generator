import logging
import os
import secrets

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_secure_key(length: int) -> str:
    """
    Produces a high-entropy, cryptographically secure random string encoded in URL-safe base64.
    Ideal for API keys, tokens, and secure identifiers in web applications.
    """
    return secrets.token_urlsafe(length)

def main():
    # Retrieve the desired key length from environment variables, defaulting to 32
    key_length = int(os.getenv('KEY_LENGTH', '32'))
    logging.info(f"Initiating secure key creation process for {key_length} byte length...")
    # Generate the key
    api_key = generate_secure_key(key_length)
    logging.info("Key generation completed without issues!")
    # Output the key to stdout for capture by the calling script
    print(api_key)

if __name__ == "__main__":
    main()