import requests
import re
import json

def scrape_7zip_version():
    try:
        # URL of the 7-Zip download page
        url = "https://www.7-zip.org/download.html"

        # Fetch the webpage content using requests
        response = requests.get(url)
        response.raise_for_status()  # Raise an error if the request fails
        html_content = response.text

        # Regex pattern to match the version ("Download 7-Zip <version>")
        match = re.search(r"Download 7-Zip (\d+\.\d+)", html_content)

        if match:
            version = match.group(1)  # Extract the version from the match
            # Prepare the result JSON-like structure
            result = {
                "productName": "7-Zip",
                "productVersion": version,
                "downloadURL": url
            }
            print(json.dumps(result))  # Output the result as JSON
        else:
            # If the regex doesn't find a match, return an error message
            error = {"status": "error", "message": "Version not found."}
            print(json.dumps(error))

    except Exception as e:
        # Handle any exceptions and return an error message
        error = {"status": "error", "message": str(e)}
        print(json.dumps(error))

if __name__ == "__main__":
    # Execute the scraping function
    scrape_7zip_version()