
---

# 📘 Post on Facebook via Python

This project demonstrates how to publish a **Facebook Page post using Python** and the **Facebook Graph API**.

---

## ⚙️ Setup

### 1️⃣ Install dependencies

```bash
pip install requests python-dotenv
```

### 2️⃣ Configure environment variables

Update `env.example.txt` with your credentials and rename it to `.env`:

```txt
FACEBOOK_ACCESS_TOKEN=your_page_access_token
FACEBOOK_PAGE_ID=your_page_id
```

* **FACEBOOK\_ACCESS\_TOKEN** → Your Page Access Token (from [Meta Developer App](https://developers.facebook.com/))
* **FACEBOOK\_PAGE\_ID** → Your Facebook Page ID

### 3️⃣ Load environment variables (Linux/macOS)

```bash
source load_env.sh
```

### 4️⃣ Run the script

```bash
python3 post_facebook.py
```

---

## 📜 Example Script (`post_facebook.py`)

```python
import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

ACCESS_TOKEN = os.getenv("FACEBOOK_ACCESS_TOKEN")
PAGE_ID = os.getenv("FACEBOOK_PAGE_ID")

def post_message(message):
    url = f"https://graph.facebook.com/{PAGE_ID}/feed"
    payload = {
        "message": message,
        "access_token": ACCESS_TOKEN
    }
    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        print("✅ Successfully posted to Facebook Page!")
    else:
        print("❌ Failed to post:", response.json())

if __name__ == "__main__":
    post_message("Hello, Facebook! 🚀 #Python #Automation")
```

---

## 📌 Notes

* This script posts a simple **text message** to your Facebook Page.
* Requires a valid **Page Access Token** with `pages_manage_posts` permission.
* You can extend it to post **links, images, or videos** using Graph API endpoints.

---
