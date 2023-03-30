from block.block import ORD
from block.hash import hash
from datetime import datetime

class ORDchain:
    """_summary_
        Blockchain validator system
    """
    def __init__(self, owner):
        self.owner = owner
        
        # init chain
        self.chain = []
        
        # init block
        block = ORD("Genesis block")
        block.hash = hash(block)
        
        # push genesis to chain
        self.chain.append(block)
        
        # Proof Of Work secret rule
        self.PoW = 4
        
    def __str__(self):
        """_summary_
            Present the owner
        """
        return f'Valitator\'s own by {self.owner}'
    
    def add_block(self, data):
        """_summary_
            Add a new block to chain
        """
        block = ORD(data)
        block.prev_hash = self.chain[-1].hash
        
        """
            Proof Of Work part
            find out specific nonce number to satisfy the rule in example
        """
        starting_time = datetime.now()
        block.hash = hash(block)
        while not self.proof_of_work(block):
            block.nonce += 1
            block.hash = hash(block)
        block.total_time = datetime.now() - starting_time
        
        self.chain.append(block)
    
    def proof_of_work(self, block):
        """_summary_
            Secret rule of our blockchain system
        """
        PoW_prefix = 'f' * self.PoW
        return block.hash.startswith(PoW_prefix)
    
    def disp(self):
        """_summary_
            Display a blockchain
        """
        for block in self.chain:
            msg = (
                f'\nData: {block.data}'
                f'\nPrevious hash: {block.prev_hash}'
                f'\nHash: {block.hash}'
                f'\nNonce: {block.nonce}'
                f'\nTime: {block.total_time}')
            print(msg)
            
    def is_valid(self):
        """_summary_
            Validate blockchain, prevent modification of transaction history
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            if not self.proof_of_work(current_block):
                return False
            if hash(current_block) != current_block.hash:
                return False
            prev_block = self.chain[i-1]
            if prev_block.hash != current_block.prev_hash:
                return False
        return True
