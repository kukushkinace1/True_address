from web3 import Web3

with open('keys.txt', 'r') as file:
    ACCOUNTS = [line.strip() for line in file]


if __name__ == '__main__':
    for acc in ACCOUNTS:
        account = Web3().eth.account.from_key(acc)
        print(account.address)
