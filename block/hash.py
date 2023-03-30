from hashlib import sha256
import json

def hash(block):
    """_summary_
        Hash a block using SHA256
    """
    data = block.data + block.prev_hash + str(block.nonce)
    data = data.encode('utf-8')     # prepare to hash
    
    return sha256(data).hexdigest() # get only hashstring