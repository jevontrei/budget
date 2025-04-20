import os
import requests

api_key = os.environ["API_KEY"]
headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
base_url = os.getenv("API_BASE_URL", "https://api.up.com.au/api/v1")

def get_accounts():
    full_url = f"{base_url}/accounts"
    
    try:
        response = requests.get(full_url, headers=headers)
        response.raise_for_status()  # this does nothing if response=2xx
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def get_an_account(accountId):
    full_url = f"{base_url}/accounts/{accountId}"
    
    try:
        response = requests.get(full_url, headers=headers)
        response.raise_for_status()  # this does nothing if response=2xx
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def get_transactions():
    full_url = f"{base_url}/transactions"

    try:
        response = requests.get(full_url, headers=headers)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


def get_a_transaction(transactionId: str):
    assert type(transactionId) == str

    full_url = f"{base_url}/transactions/{transactionId}"
    try:
        response = requests.get(full_url, headers=headers)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


def add_tag(transactionId: str, tag: dict) -> dict:
    assert type(transactionId) == str
    assert type(tag) == dict

    full_url = f"{base_url}/transactions/{transactionId}/relationships/tags"

    try:
        response = requests.post(url=full_url, headers=headers, json=tag)
        response.raise_for_status()
        assert type(response) == requests.models.Response
        # Don't use response.json() because there's no response content, just a success code
        return response

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
