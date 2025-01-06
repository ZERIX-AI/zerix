import json
import os
import time

import click
from web3 import Web3

import app
from extensions.ext_database import db
from models.token import AccountTokenBalance, AccountTokenLog, TokenLogType

file_path = os.path.join(os.getcwd(), 'storage/deposit/')
w3 = Web3(Web3.HTTPProvider("https://sepolia.era.zksync.dev"))

with open(file_path + 'ZERIXAI.json', 'r') as abi_file:
    data = json.load(abi_file)
    contract = w3.eth.contract(address=data["address"], abi=data["abi"])


@app.celery.task(queue="dataset", acks_late=True)
def token_deposit_detector_task():
    start_at = time.perf_counter()

    try:
        # start polling from the saved block
        with open(file_path + 'info.json', 'r') as deposit_file:
            deposit_data = json.load(deposit_file)

        deposit_address = deposit_data["deposit_address"]
        saved_block = deposit_data["saved_block_number"]
        new_block = w3.eth.get_block('latest')['number']
        if new_block > saved_block:
            print(f"New block detected, scanning from {saved_block + 1} to {new_block}...")
            events = contract.events.Transfer().get_logs(from_block=saved_block + 1, to_block=new_block)
            for event in events:
                to = event['args']['to'].lower()
                if to == deposit_address:
                    handle_deposit(event['args']['from'], event['args']['value'], '0x' + event['transactionHash'].hex())

            # save the new block number
            with open(file_path + 'info.json', 'w') as deposit_file:
                deposit_data["saved_block_number"] = new_block
                json.dump(deposit_data, deposit_file)

            end_at = time.perf_counter()
            click.echo(click.style("Token deposit detector done. latency: {}".format(end_at - start_at), fg="green"))

        else:
            click.echo(click.style("No new block detected.", fg="green"))
    except Exception as e:
        click.echo(
            click.style("Token deposit detector error: {} {}".format(e.__class__.__name__, str(e)), fg="red")
        )


def handle_deposit(from_address, value, tx_hash):
    from_address = from_address.lower()
    amount = Web3.from_wei(value, 'ether')
    print(f'Deposit Event: From: {from_address}, Amount: {amount}, TxHash: {tx_hash}')
    try:
        # add log
        new_log = AccountTokenLog()
        new_log.address = from_address
        new_log.amount = amount
        new_log.tx_hash = tx_hash
        new_log.log_type = TokenLogType.DEPOSIT
        db.session.add(new_log)
        db.session.commit()
    except Exception as e:
        if 'unique constraint' in str(e):
            return

    # update balance
    dataset_query = (db.session.query(AccountTokenBalance).filter(AccountTokenBalance.address == from_address).first())
    if not dataset_query:
        new_balance = AccountTokenBalance()
        new_balance.address = from_address
        new_balance.balance = amount
        db.session.add(new_balance)
        db.session.commit()
    else:
        dataset_query.balance += amount
        db.session.commit()
