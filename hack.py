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