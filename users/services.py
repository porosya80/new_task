from django.conf import settings
import requests
from pyhunter import PyHunter


def get_details(email):
    url = "https://person.clearbit.com/v2/people/find"
    api_key = settings.API_KEY
    params = {'email': email}
    headers = {
        'Authorization': f"Bearer {api_key}",
    }
    r = requests.request("GET", url, headers=headers, params=params)
    details = r.json()

    return r.json()



def check_email(email):
    HUNT_KEY = settings.HUNT_KEY
    hunter = PyHunter(HUNT_KEY)
    result = hunter.email_verifier(email)

    return True if result['result'] == 'undeliverable' else False
