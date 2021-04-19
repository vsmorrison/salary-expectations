import os
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.getenv('secret_key')
