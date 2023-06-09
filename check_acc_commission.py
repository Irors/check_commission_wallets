import time
import loguru
import requests
import web3
from web3 import Web3

bnb = eth = ftm = arb = polygon = avax = 0

with open("wallets.txt") as wallet:
    wallets = wallet.readlines()

with open("arb_api_key.txt") as arb_api:
    arb_key = arb_api.readline()

with open("avax_api_key.txt") as avax_api:
    avax_key = avax_api.readline()

with open("bsc_api_key.txt") as bsc_api:
    bsc_key = bsc_api.readline()

with open("eth_api_key.txt") as eth_api:
    eth_key = eth_api.readline()

with open("ftm_api_key.txt") as ftm_api:
    ftm_key = ftm_api.readline()

with open("polygon_api_key.txt") as polygon_api:
    polygon_key = polygon_api.readline()

contract_addr = {"0xaa9c15cd603428ca8ddd45e933f8efe3afbcc173"}

for adresss in wallets:
    #bnb = eth = ftm = arb = polygon = avax = 0

    if adresss == wallets[-1]:
        response_bsc = requests.get(
            f"https://api.bscscan.com/api?module=account&action=txlist&address={adresss}&startblock=0&endblock=99999999&page=1&offset=1000&sort=asc&apikey={bsc_key}")
        response_eth = requests.get(
            f"https://api.etherscan.com/api?module=account&action=txlist&address={adresss}&startblock=0&endblock=99999999&page=1&offset=1000&sort=asc&apikey={eth_key}")
        response_ftm = requests.get(
            f"https://api.ftmscan.com/api?module=account&action=txlist&address={adresss}&startblock=0&endblock=99999999&page=1&offset=1000&sort=asc&apikey={ftm_key}")
        response_arb = requests.get(
            f"https://api.arbiscan.io/api?module=account&action=txlist&address={adresss}&startblock=0&endblock=99999999&page=1&offset=1000&sort=asc&apikey={arb_key}")
        response_polygon = requests.get(
            f"https://api.polygonscan.com/api?module=account&action=txlist&address={adresss}&startblock=0&endblock=99999999&page=1&offset=1000&sort=asc&apikey={polygon_key}")
        response_avax = requests.get(
            f"https://api.snowtrace.io/api?module=account&action=txlist&address={adresss}&startblock=0&endblock=99999999&page=1&offset=1000&sort=asc&apikey={avax_key}")

    else:
        response_bsc = requests.get(
            f"https://api.bscscan.com/api?module=account&action=txlist&address={adresss[:-1]}&startblock=0&endblock=99999999&page=1&offset=1000&sort=asc&apikey={bsc_key}")
        response_eth = requests.get(
            f"https://api.etherscan.com/api?module=account&action=txlist&address={adresss[:-1]}&startblock=0&endblock=99999999&page=1&offset=1000&sort=asc&apikey={eth_key}")
        response_ftm = requests.get(
            f"https://api.ftmscan.com/api?module=account&action=txlist&address={adresss[:-1]}&startblock=0&endblock=99999999&page=1&offset=1000&sort=asc&apikey={ftm_key}")
        response_arb = requests.get(
            f"https://api.arbiscan.io/api?module=account&action=txlist&address={adresss[:-1]}&startblock=0&endblock=99999999&page=1&offset=1000&sort=asc&apikey={arb_key}")
        response_polygon = requests.get(
            f"https://api.polygonscan.com/api?module=account&action=txlist&address={adresss[:-1]}&startblock=0&endblock=99999999&page=1&offset=1000&sort=asc&apikey={polygon_key}")
        response_avax = requests.get(
            f"https://api.snowtrace.io/api?module=account&action=txlist&address={adresss[:-1]}&startblock=0&endblock=99999999&page=1&offset=1000&sort=asc&apikey={avax_key}")


    print(f"\nAccount {adresss}")

    ###
    try:
        for acc in response_bsc.json()['result']:
            if int(acc['nonce']) < 500:
                if acc['to'] not in contract_addr:
                    bnb += int(acc['gasUsed']) * int(acc['gasPrice']) / 10**18 + int(acc['value']) / 10 ** 18
        print(bnb, "потрачено bnb")
    except:
        print("0 транзакций")

    ###
    try:
        for acc in response_eth.json()['result']:
            if int(acc['nonce']) < 500:
                if acc['to'] not in contract_addr:
                    eth += (int(acc['gasPrice']) * int(acc['gasUsed']) / 10**18) + (int(acc['value']) / 10 ** 18)
        print(eth, "потрачено eth")
    except:
        print("0 транзакций")

    ###
    try:
        for acc in response_ftm.json()['result']:
            if int(acc['nonce']) < 500:
                if acc['to'] not in contract_addr:
                    ftm += (int(acc['gasPrice']) * int(acc['gasUsed']) / 10**18) + (int(acc['value']) / 10 ** 18)
        print(ftm, "потрачено ftm")
    except:
        print("0 транзакций")


    ###
    try:
        for acc in response_arb.json()['result']:
            if int(acc['nonce']) < 500:
                if acc['to'] not in contract_addr:
                    arb += (int(acc['gasPriceBid']) * int(acc['gasUsed']) / 10 ** 18) + (int(acc['value']) / 10 ** 18)
        print(arb, "потрачено arb_eth")
    except:
        print("0 транзакций")


    ###
    try:
        for acc in response_polygon.json()['result']:
            if int(acc['nonce']) < 500:
                if acc['to'] not in contract_addr:
                    polygon += (int(acc['gasPrice']) * int(acc['gasUsed']) / 10**18) + (int(acc['value']) / 10 ** 18)
        print(polygon, "потрачено matic")
    except:
        print("0 транзакций")

    ###
    try:
        for acc in response_avax.json()['result']:
            if int(acc['nonce']) < 500:
                if acc['to'] not in contract_addr:
                    avax += ((int(acc['gasPrice']) * int(acc['gasUsed'])) / 10**18) + (int(acc['value']) / 10 ** 18)
        print(avax, "потрачено avax")
    except:
        print("0 транзакций")

