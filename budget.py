# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "requests",
#   "pydantic",
# ]
# ///

import os
import requests
import json
from typing import Any
from pydantic import BaseModel
from enum import Enum

os.system("clear")

api_key = os.environ["API_KEY"]
headers = {"Authorization": f"Bearer {api_key}"}

base_url = os.getenv("API_BASE_URL", "https://api.up.com.au/api/v1")


class API_type(Enum):
    ACCOUNTS = "accounts"
    TRANSACTIONS = "transactions"
    PING = "util/ping"


def get_data(data: str) -> dict:
    full_url = f"{base_url}/{data.value}"

    try:
        response = requests.get(full_url, headers=headers)
        response.raise_for_status()  # understand this
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


# response = get_data(API_type.ACCOUNTS)
# response = get_data(API_type.TRANSACTIONS)
response = get_data(API_type.PING)

# # why do i get type=dict when i used .json()?
# -> it's  bc .json() is deserialising the response JSON for me

if not response:  # this guard clause not work how i thought, i.e. when all `response = get_data()` lines above are commented out
    print("No response.")
else:
    print(f"Retrieved {len(response)} item/s in response...")
    print("-" * 50)
    print(response.keys())
    print("-" * 50)
    if "data" in response and response["data"]:
        print(
            f"Retrieved {len(response['data'])} item/s in response['data']...")
        for item in response["data"]:
            print(item)
            print("-" * 50)

########################################################


def edit_tag(transactionId: str, tag: str) -> dict:
    full_url = f"{base_url}/transactions/{transactionId}/relationships/tags"
    print("full url =", full_url)

    try:
        # this is broken; error 422; but it works in insomnia
        # -> something wrong with my args? params=?
        # response = requests.post(url=full_url, headers=headers, data=tag, params=)
        response = requests.patch(url=full_url, headers=headers, data=tag)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


transactionId = "207f6db9-888d-4bd9-afd9-73ec3e02c382"
tag = {
    "data": [
        {
            "type": "tags",
            "id": "testFromLaptop2"
        }
    ]
}

response = edit_tag(transactionId=transactionId, tag=json.dumps(tag))

if not response:
    # print("No response.")
    pass
else:
    print(response)

print()

# get transaction to check edited tag [make this just get tag]
r = requests.get(
    f"https://api.up.com.au/api/v1/transactions/{transactionId}", headers=headers)
print(f"transaction\n{r.content}\n")
