import os
import requests

# Load environment variables
access_token = os.getenv("FACEBOOK_ACCESS_TOKEN")
page_id = os.getenv("FACEBOOK_PAGE_ID")  # Facebook Page ID

url = f"https://graph.facebook.com/{page_id}/feed"

post_data = {
    "message": "Hello Facebook 👋 - This post was published directly using Python! 🚀",
    "access_token": access_token
}

response = requests.post(url, data=post_data)

if response.status_code == 200:
    print("✅ Post created successfully on Facebook!")
    print(response.json())
else:
    print(f"❌ Failed to post. Status: {response.status_code}, Response: {response.text}")
