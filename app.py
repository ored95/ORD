from blockchain import ORDchain
from block.hash import hash

# test a simple blockchain
blockchain = ORDchain("ored95")
print(blockchain)
blockchain.add_block("Binh Nguyen")
blockchain.add_block("Alex Nguyen")
blockchain.add_block("BMSTU iu7")
blockchain.disp()

"""
A hacker is trying to hack our blockchain system.
And somehow he knew our secret rule. Then, he attempted
to modify our blockchain data in order to pass the validator.
This is what he did.
"""
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
