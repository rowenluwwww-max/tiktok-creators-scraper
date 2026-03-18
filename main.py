import requests
import re
import time
import json
from datetime import datetime

class TikTokCreatorScraper:
    def __init__(self):
        self.session = requests.Session()

    def extract_email(self, bio):
        # Regex to find email addresses in the bio
        email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        email = re.findall(email_regex, bio)
        return email[0] if email else None

    def scrape_creators(self, creators):
        results = []
        for creator in creators:
            response = self.session.get(creator['profile_url'])
            # Assuming `bio` is extracted from the response
            bio = response.json().get('bio')
            email = self.extract_email(bio)
            results.append({'username': creator['username'], 'email': email})
        return results

    def save_to_json(self, data):
        filename = 'tiktok_creators_' + datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.json'
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)