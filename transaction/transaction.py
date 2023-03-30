import json
class Transaction:
    """_summary_
        Transaction definition
        - from: who sent?
        - to: who received?
        - amount: total ORD?
    """
    def __init__(self, records):
        self.details = []
        if type(records) == dict:
            self.details.append(records)
        elif type(records) == list:
            self.details = records
        
    def __str__(self):
        return json.dumps(self.details)
