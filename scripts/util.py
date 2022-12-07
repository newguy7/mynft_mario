from brownie import accounts, network, config


def get_account():
    if (
        network.show_active() == "development"
    ):  # if working in the local chain or ganache, we can select the position of account.
        return accounts[0]

    # if network.show_active() in ["development", "ganache-local"]:
    #     return accounts[0]

    else:
        return accounts.add(config["wallets"]["from_key"])
