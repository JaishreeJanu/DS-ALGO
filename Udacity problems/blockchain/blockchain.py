import hashlib
import datetime
import time

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime())
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash(data)
      self.next = None


    def calc_hash(self,data):
      sha = hashlib.sha256()
      hash_str = data.encode('utf-8')
      sha.update(hash_str)
      return sha.hexdigest()


def create_blockchain(blockchain_list):
        Head = None
        curr_block = None
        for block in blockchain_list:
            new_block = Block(block['timestamp'], block['data'], None)
            if Head is None:
                Head = new_block
                curr_block = Head
            else:
                new_block.previous_hash = curr_block.hash
                curr_block.next = new_block
                curr_block = curr_block.next

        return Head


blockchain_list = [{
    'timestamp': None,
    'data': "This start block. I am linked list.",
    'previous_hash': None,
    'hash': None
},
{
    'timestamp': None,
    'data': "I am hash table.",
    'previous_hash': None,
    'hash': None
},
{
    'timestamp': None,
    'data': "I am binary search tree.",
    'previous_hash': None,
    'hash': None
},
{
    'timestamp': None,
    'data': "I am hash map.",
    'previous_hash': None,
    'hash': None
}]

head = create_blockchain(blockchain_list)

while head:
    print("-"*15)
    print(head.data)
    print(head.previous_hash)
    print(head.timestamp)
    head = head.next






