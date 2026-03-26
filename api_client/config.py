import os

BASE_URL = "https://jsonplaceholder.typicode.com"

POSTS_ENDPOINT = "/posts"

API_KEY=os.getenv("API_KEY", "bridgelabz")

DEFAULT_HEADERS={
    "Content-Type":"application/json",
    "Authorization":f"Bearer {API_KEY}"
}

REQUEST_TIMEOUT=5