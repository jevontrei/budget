# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "requests",
#   "pydantic",
# ]
# ///

import os
from datetime import datetime
import time
import requests
import json
from typing import Any
from pydantic import BaseModel
from enum import Enum

from utils import add_tag, get_a_transaction, get_transactions, get_accounts, get_an_account
# from get_data import get_data

os.system("clear")


def main():
    # try:
    while True:
        print()
        print("-" * 50)
        print("Hi! What do you wanna do?\n")
        print("0. Check spending balance")
        print("1. Get accounts")
        print("10. Get an account")
        print("2. Get a transaction")
        print("20. Get transactions")
        print("3. Add a tag to a transaction")
        print("4. Clear terminal")
        print("5. What's the time?")
        print("6. Read me a poem")
        print("7. Exit\n")

        selection = input("Select a number: ")
        selection = int(selection.strip())
        print()

        match selection:
            case 0:
                # Firstly, present all accounts and let user choose one
                accounts = get_accounts()
                if not accounts:
                    print("Oops")
                else:
                    count = 1
                    print("Available accounts:")
                    for account in accounts["data"]:
                        print(f"{count}. {account['attributes']['displayName']}")
                        count += 1
                    print()

                selected_account = input("Select an account (1, 2, 3 etc): ")
                selected_account = int(selected_account.strip())
                print()

                if selected_account in range(1, len(accounts) + 1):
                    account = accounts["data"][selected_account - 1]
                    print(f"Balance: {account['attributes']['balance']['value']} {account['attributes']['balance']['currencyCode']}")
                else:
                    print("Sorry, that number doesn't make sense to me.")
                    continue

            case 1:
                response = get_accounts()
                if not response:
                    print("No response.")
                else:
                    for account in response["data"]:
                        print(f"\n{account}")

            case 10:
                
                
                accountId = input("Enter an accountId, or press Enter to use a default: ")
                accountId = accountId or "32a5fadd-4432-449e-8a30-782648cb2336"
                print()
                
                response = get_an_account(accountId)
                if not response:
                    print("No response.")
                else:
                    print(f"{response}")

            case 2:
                transactionId = input("Enter a transactionId, or press Enter to use a default: ")
                transactionId = transactionId or "207f6db9-888d-4bd9-afd9-73ec3e02c382"

                response = get_a_transaction(transactionId)
                if not response:
                    print("No response.")
                else:
                    print(f"{response}")

            case 20:
                response = get_transactions()

                if not response:
                    print("No response.")
                else:
                    for transaction in response["data"]:
                        print(f"\n{transaction}")

            case 3:
                transactionId = input("Enter a transactionId, or press Enter to use a default: ")
                transactionId = transactionId or "207f6db9-888d-4bd9-afd9-73ec3e02c382"

                tagId = input("Enter your tag, or press Enter to use a default: ")
                tagId = str(tagId) or f"test{int(time.time())}"
                tag = {"data": [{"type": "tags", "id": tagId}]}

                add_tag(transactionId=transactionId, tag=tag)
                # response = add_tag(transactionId=transactionId, tag=tag)
                print()

                print("Now let's see our hard work...\n")
                tags = get_a_transaction(transactionId)["data"]["relationships"]["tags"]["data"]
                if not tags:
                    print("Oops")
                else:
                    for tag in tags:
                        print(tag)

            case 4:
                os.system("clear")

            case 5:
                print(datetime.now())

                epoch_time = int(time.time())
                print("Number of non-leap seconds that have elapsed since 00:00:00 UTC on 1 January 1970:", epoch_time)

            case 6:
                import this

            case 7:
                print("Bye!")
                return


# except Exception as e:
#     print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
