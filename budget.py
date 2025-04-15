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

# MU:
# 1. find out what pydantic is
# data ~validation library

# 2. why might you want to use it
# to make it easy to pass valid values into a function or other thing

# 3. create types for the up apis


class API_type(Enum):
    ACCOUNTS = "accounts"
    TRANSACTIONS = "transactions"
    PING = "util/ping"

# 4. make fn that takes an enum and returns the appropriate data type


def get_data(data: str) -> dict:
    base_url = os.getenv("API_BASE_URL", "https://api.up.com.au/api/v1")
    full_url = f"{base_url}/{data.value}"

    try:
        return requests.get(full_url, headers=headers).json()
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


response = get_data(API_type.ACCOUNTS)
# response = get_data(API_type.TRANSACTIONS)
# response = get_data(API_type.PING)
# why do i get type=dict when i used .json()? they look identical to me but i thought they not same. does the `-> dict` force it?
if response:
    print(f"Retrieved {len(response)} item/s")
    print()
    for each in response:
        # print(f"Item ...")
        print(f"{each}\n{type(each)}")
        print(f"{response}\n{type(response)}")
        print("-" * 50)
else:
    print("No response.")

#############################################################
# MISC REQUESTS TO INTEGRATE

# get a transaction
# r = requests.get(
#     "https://api.up.com.au/api/v1/transactions/4ced5c33-1d57-4747-9038-de8fe0367539", headers=headers)
# print(f"transaction\n{r.content}\n")

# get transactions by category
# r = requests.get("https://api.up.com.au/api/v1/transactions/?filter[category]=health-and-medical", headers=headers)
# print(f"health-and-medical transactions\n{r.text}\n")

# get a transaction's category
# response = requests.get(
#     "https://api.up.com.au/api/v1/transactions/4ced5c33-1d57-4747-9038-de8fe0367539", headers=headers)
# this was a pain in the ass to find which json keys to use; surely there's a better way?:
# print(
#     response.json()["data"]["attributes"]["amount"]["value"],
#     response.json()["data"]["relationships"]["category"]["data"]["id"]
# )

# just snooping:
# print(response.encoding) # utf-8
