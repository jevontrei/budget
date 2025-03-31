import os
import requests

api_key = os.environ["API_KEY"]

headers = {"Authorization": f"Bearer {api_key}"}

# # test api key
# r = requests.get("https://api.up.com.au/api/v1/util/ping", headers=headers)
# print(f"\n{r.text}\n")

# # get accounts
# r = requests.get("https://api.up.com.au/api/v1/accounts", headers=headers)
# print(f"\n{r.text}\n")

# # get transactions
# r = requests.get("https://api.up.com.au/api/v1/transactions", headers=headers)
# print(f"\n{r.text}\n")

# # get a transaction
# r = requests.get("https://api.up.com.au/api/v1/transactions/4ced5c33-1d57-4747-9038-de8fe0367539", headers=headers)
# print(f"\n{r.text}\n")

# # get a transaction's category
r = requests.get("https://api.up.com.au/api/v1/transactions/4ced5c33-1d57-4747-9038-de8fe0367539", headers=headers)
print(f"\n{r.text}\n")

# get a transaction's category
# r = requests.get("https://api.up.com.au/api/v1/transactions/?filter[category]=health-and-medical", headers=headers)
# print(f"\n{r.text}\n")
