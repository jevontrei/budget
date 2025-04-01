# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "requests",
#   "pydantic",
# ]
# ///

import os
import requests
from pydantic import BaseModel
from enum import Enum

os.system("clear")

print()

api_key = os.environ["API_KEY"]
headers = {"Authorization": f"Bearer {api_key}"}

# # test api key
# r = requests.get("https://api.up.com.au/api/v1/util/ping", headers=headers)
# print(f"testing api key\n{r.text}\n")

# # get accounts
# r = requests.get("https://api.up.com.au/api/v1/accounts", headers=headers)
# print(f"accounts\n{r.content}\n")

# # get transactions
# # r = requests.get("https://api.up.com.au/api/v1/transactions", headers=headers)
# # print(f"transactions\n{r.text}\n")

# # get a transaction
# r = requests.get(
#     "https://api.up.com.au/api/v1/transactions/4ced5c33-1d57-4747-9038-de8fe0367539", headers=headers)
# print(f"transaction\n{r.content}\n")

# # # get transactions by category
# r = requests.get("https://api.up.com.au/api/v1/transactions/?filter[category]=health-and-medical", headers=headers)
# # print(f"health-and-medical transactions\n{r.text}\n")

# # # get a transaction's category
# response = requests.get(
#     "https://api.up.com.au/api/v1/transactions/4ced5c33-1d57-4747-9038-de8fe0367539", headers=headers)
# # # this was a pain in the ass to find which json keys to use:
# print(
#     response.json()["data"]["attributes"]["amount"]["value"],
#     response.json()["data"]["relationships"]["category"]["data"]["id"]
# )

# # just snooping:
# print(response.encoding) # utf-8

#######################################################################

# MU:
# 1. find out what pydantic is
# data validation library

# 2. why might you want to use it
##

# 3. create types for the up apis
##


class API_type(Enum):
    ACCOUNTS = "accounts"
    TRANSACTIONS = "transactions"
    PING = "util/ping"


# print((API_type.ACCOUNTS.value))


class Hmmm(BaseModel):
    ...

# 4. make fn that takes an enum and returns the appropirate data type
##


def get_data(data: str) -> dict:
    match data:
        case "accounts":
            return requests.get(
                f"https://api.up.com.au/api/v1/{data}",
                headers=headers
            ).json()

        case "transactions":
            return requests.get(
                f"https://api.up.com.au/api/v1/{data}",
                headers=headers
            ).json()

        case "util/ping":
            return requests.get(
                f"https://api.up.com.au/api/v1/{data}",
                headers=headers
            ).json()


response = get_data(API_type.ACCOUNTS.value)
print(response)
# print(f"response: {response}, {type(response)}")

response = get_data(API_type.TRANSACTIONS.value)
print(response)

response = get_data(API_type.PING.value)
print(response)

print()
