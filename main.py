"""
Main file containing the full code to running the RPA
"""

# Imports
from dotenv import load_dotenv
import os

if __name__ == '__main__':

    # Credentials
    load_dotenv('credentials.env')

    user_name = os.getenv('USER_NAME')
    password = os.getenv('PASSWORD')

    print(user_name)
    print(password)