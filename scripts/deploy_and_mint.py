from brownie import MarioNFT, config, network
from scripts.util import get_account
from scripts.create_metadata import create_metadata

sample_token_uri = "https://ipfs.io/ipfs/{}?filename={}"


def deploy_and_mint():
    account = get_account()
    marionft = MarioNFT.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    # marionft = MarioNFT[-1]

    metadatas = create_metadata()

    for metadata in metadatas:
        token_uri = sample_token_uri.format(metadata["CID"], metadata["filename"])
        tx = marionft.createLogoNFT(token_uri, {"from": account})
        tx.wait(1)

        print("New token has been created!")


def main():
    deploy_and_mint()
