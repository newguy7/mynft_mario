import os
import json

# from scripts.pinata import pinata_upload, get_pinned
import scripts.pinata as p


def create_metadata():
    imgDir = ".\\imgs"
    metadatas = []

    pinnedFiles = p.get_pinned()

    for idx, file in enumerate(os.listdir(imgDir)):
        filepath = os.path.join(imgDir, file)
        logoName = file.split(".")[0]
        metadataFile = f"{logoName}.json"
        metadataFilePath = f".\\Metadata\\{metadataFile}"

        if metadataFile in pinnedFiles:
            metadatas.append(
                {"filename": metadataFile, "CID": pinnedFiles[metadataFile]}
            )
            continue

        result = p.pinata_upload(filepath)
        imgCID = result["IpfsHash"]

        metadata = {
            "name": logoName,
            "description": f"Super Mario Bros logo: {logoName}",
            "image": imgCID,
            "attributes": [
                {"trait_type": "Rank", "value": idx + 1},
                {"trait_type": "strength_level", "value": 100},
                {"trait_type": "damage_level", "value": 20},
            ],
        }

        with open(metadataFilePath, "w") as f:
            json.dump(metadata, f)

        result = p.pinata_upload(metadataFilePath)
        metadatas.append({"filename": metadataFile, "CID": result["IpfsHash"]})

    return metadatas


def main():
    metadatas = create_metadata()
    print(metadatas)
