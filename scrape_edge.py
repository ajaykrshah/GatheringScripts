import sys
import requests
from bs4 import BeautifulSoup
import re
import json

def scrape_microsoft_edge(url):
    try:
        # Fetch HTML content from the URL
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text

        # Parse HTML using BeautifulSoup or Regex
        match = re.search(r'"Product&quot;:&quot;Stable&quot.+?Releases.+?ProductVersion.+?:(.+?)(\d+\.\d+\.\d+\.\d+)"', html_content, re.MULTILINE)

        # Extract necessary details
        product_id = 79
        product_name = "Microsoft Edge"
        product_version = match.group(2) if match else "Unknown"
        download_url = "https://www.microsoft.com/en-us/edge/business/download"

        # Prepare the JSON result
        result = {
            "productID": product_id,
            "productName": product_name,
            "productVersion": product_version,
            "downloadURL": download_url,
        }

        return result

    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"status": "error", "message": "No URL provided"}))
        sys.exit(1)

    scraping_url = sys.argv[1]
    print(json.dumps(scrape_microsoft_edge(scraping_url)))
