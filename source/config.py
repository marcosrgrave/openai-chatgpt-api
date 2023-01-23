from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_KEY: str = getenv("API_KEY")
