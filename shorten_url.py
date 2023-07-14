import requests
import json

def shorten_url(url, access_token):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "long_url": url
    }
    
    response = requests.post("https://api-ssl.bitly.com/v4/shorten", headers=headers, data=json.dumps(payload))
    data = response.json()
    
    if response.status_code == 200:
        return data.get("link")
    else:
        print("Error occurred:", data.get("message", "Unknown error"))
        return None

# Replace ACCESS_TOKEN with your actual bit.ly API access token
access_token = "b76aab68382e108e80c4f795a3e5aef25b1d2227"
long_url = "https://oceana.market"

short_url = shorten_url(long_url, access_token)
if short_url:
    print("Shortened URL:", short_url)
