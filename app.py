from blockchain import ORDchain
from block.hash import hash
from transaction.transaction import Transaction

# demo transaction (assumming that all transactions are valid)
transaction_03_31 = Transaction([
    {"from": "jame", "to": "ored95", "amount": 1000},
    {"from": "ored95", "to": "alex", "amount": 100},
    {"from": "ored95", "to": "john wick", "amount": 500}])

transaction_04_01 = Transaction([
    {"from": "maria", "to": "ored95", "amount": 200},
    {"from": "ored95", "to": "kate", "amount": 300}])

# test a simple blockchain
blockchain = ORDchain("ored95")
print(blockchain)
blockchain.add_block(transaction_03_31.details)
blockchain.add_block(transaction_04_01.details)
blockchain.disp()

wallet_addr = "ored95"
print(f'\nWallet address [{wallet_addr}]\'s balance: {blockchain.get_balance(wallet_addr)} ORD')
