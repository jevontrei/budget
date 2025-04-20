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

from utils import add_tag, get_a_transaction  # , get_accounts, get_transactions
# from get_data import get_data

os.system("clear")


def main():
    # try:
    while True:
        print()
        print("-" * 50)
        print("Hi! What do you wanna do?")
        print("0. Check balance")
        print("1. Get accounts")
        print("2. Get a transaction")
        print("20. Get transactions")
        print("3. Add a tag to a transaction")
        print("4. Clear terminal")
        print("5. What's the time?")
        print("6. Read me a poem")
        print("7. Exit")
        print()

        selection = input("Select a number: ")
        selection = int(selection.strip())
        print()

        match selection:
            case 0:
                ...
                # get_balance()

            case 1:
                ...
                # get_accounts()

            case 2:
                transactionId = input("Enter a transactionId, or press Enter to use the default: ")
                transactionId = transactionId or "207f6db9-888d-4bd9-afd9-73ec3e02c382"

                get_a_transaction(transactionId)

            case 20:
                ...
                # get_transactions()

            case 3:
                transactionId = input("Enter a transactionId, or press Enter to use a default: ")
                transactionId = transactionId or "207f6db9-888d-4bd9-afd9-73ec3e02c382"

                tagId = input("Enter your tag, or press Enter to use a default: ")
                tagId = str(tagId) or f"test{int(time.time())}"
                tag = {"data": [{"type": "tags", "id": tagId}]}

                response = add_tag(transactionId=transactionId, tag=tag)
                print()

                print("Now let's see our hard work...")
                print()
                tags = get_a_transaction(transactionId)["data"]["relationships"]["tags"]["data"]
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
