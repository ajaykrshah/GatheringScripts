# scrape_edge.py
import sys
import requests
import re
import json

def scrape_microsoft_edge(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text

        # Extract using regex
        match = re.search(r'"Product&quot;:&quot;Stable&quot.+?Releases.+?ProductVersion.+?:(.+?)(\d+\.\d+)"', html_content)

        product_id = 79
        product_name = "Microsoft Edge"
        product_version = match.group(2) if match else "Unknown"
        download_url = "https://www.microsoft.com/en-us/edge/business/download"

        # JSON output
        result = {
            "productID": product_id,
            "productName": product_name,
            "productVersion": product_version,
            "downloadURL": download_url
        }

        print(json.dumps(result))

    except Exception as e:
        print(json.dumps({"status": "error", "message": str(e)}))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"status": "error", "message": "No URL provided"}))
        sys.exit(1)

    url = sys.argv[1]
    scrape_microsoft_edge(url)
