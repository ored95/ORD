"""
A hacker is trying to hack our blockchain system.
And somehow he knew our secret rule. Then, he attempted
to modify our blockchain data in order to pass the validator.
This is what he did.

Example from lastest [app.py]:

blockchain.chain[1].data = "Binh"
for i in range(1, len(blockchain.chain)):
    blockchain.chain[i].prev_hash = blockchain.chain[i-1].hash
    blockchain.chain[i].hash = hash(blockchain.chain[i])
    blockchain.chain[i].nonce = 0
    while not blockchain.chain[i].hash.startswith('ffff'):
        blockchain.chain[i].nonce += 1
        blockchain.chain[i].hash = hash(blockchain.chain[i])

print(f'\nHacked? {blockchain.is_valid()}')
print('-------------------------------------------------')
blockchain.disp()

TODO: hack new block datatype (change transaction history)
"""
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
wallet_addr = 'ored95'
blockchain = ORDchain(wallet_addr)
print(blockchain)
blockchain.add_block(transaction_03_31.details)
blockchain.add_block(transaction_04_01.details)
blockchain.disp()
print(f'\nBalance of owner [{blockchain.owner}]: {blockchain.get_balance(blockchain.owner)} ORD')

blockchain.chain[1].data[0]["amount"] = 2000
for i in range(1, len(blockchain.chain)):
    blockchain.chain[i].prev_hash = blockchain.chain[i-1].hash
    blockchain.chain[i].nonce = 0
    blockchain.chain[i].hash = hash(blockchain.chain[i])
    while not blockchain.chain[i].hash.startswith('ffff'):
        blockchain.chain[i].nonce += 1
        blockchain.chain[i].hash = hash(blockchain.chain[i])

print('-'*32)
print(f'!!! Hacked status: {blockchain.is_valid()}')
print('-'*32)
blockchain.disp()
print(f'\nBalance of owner [{blockchain.owner}]: {blockchain.get_balance(blockchain.owner)} ORD')
