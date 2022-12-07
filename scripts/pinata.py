import os
import requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
headers = {
    "pinata_api_key": os.getenv("PINATA_API_KEY"),
    "pinata_secret_api_key": os.getenv("PINATA_API_SECRET"),
}


def pinata_upload(filepath):
    filename = filepath.split("\\")[-1:][0]

    PINATA_BASE_URL = "https://api.pinata.cloud/"
    endpoint = "pinning/pinFileToIPFS"

    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        response = requests.post(
            PINATA_BASE_URL + endpoint,
            files={"file": (filename, image_binary)},
            headers=headers,
        )

    return response.json()


def get_pinned():
    response = requests.get(
        "https://api.pinata.cloud/data/pinList?status=pinned", headers=headers
    ).json()
    pinnedData = {}
    fileCount = response["count"]
    files = response["rows"]

    for file in files:
        filename = file["metadata"]["name"]
        pinnedData[filename] = file["ipfs_pin_hash"]

    return pinnedData


def main():
    filesPinned = get_pinned()

    for key, value in filesPinned.items():
        print(key, value)
