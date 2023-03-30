class ORD:
    """_summary_
        ORD block definition
    """
    def __init__(self, data):
        self.data = data
        self.prev_hash = ""
        self.hash = ""
        # POW: an extra random number to be satisfied by specific rule
        # for example: hash(data + nonce) = 0x0000...
        self.nonce = 0
        self.total_time = 0