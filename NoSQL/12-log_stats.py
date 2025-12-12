#!/usr/bin/env python3
"""log stats"""


from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient()
    col = client.logs.nginx

    total = col.count_documents({})
    print(f"{total} logs")
    print("Methods:")

    for m in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print(f"\tmethod {m}: {col.count_documents({'method': m})}")

    status = col.count_documents({"method": "GET", "path": "/status"})
    print(f"{status} status check")
