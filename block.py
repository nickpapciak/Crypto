from hashlib import sha256
import time


class Block:
    def __init__(self, index, prev_hash, data, nonce, timestamp=None):
        self.index = index  # current transaction in the list
        self.prev_hash = prev_hash  # previous block's hash
        self.data = data  # transaction data
        self.nonce = nonce  # proof number
        self.timestamp = timestamp or time.time()
        self.transactions = []

    @property
    def hash(self):
        return sha256(f"{self.index}{self.prev_hash}{self.timestamp}{self.data}{self.nonce}".encode()).hexdigest()

    def new_transaction(self, sender, recipient, amount):
        transaction = {
            "sender": sender,
            "recipient": recipient,
            "amount": amount
        }
        self.transactions.append(transaction)

    def block_info(self):
        return {
            "index": self.index,
            "previous_hash": self.prev_hash,
            "timestamp": self.timestamp,
            "transactions": self.transactions or None,
            "nonce": self.nonce
        }


block = Block(index=0, prev_hash="", data=[], nonce=0)
print(block.block_info())
block.new_transaction("user 1", "user 2", 0)
print(block.block_info())
print(block.hash)

# print(bin(int(sha256("".encode()).hexdigest(), 16)))


# http://www.righto.com/2014/09/mining-bitcoin-with-pencil-and-paper.html
# https://www.google.com/search?q=crypto+hash+contents&tbm=isch&ved=2ahUKEwiSqfbl8szuAhURG6wKHYMqCIAQ2-cCegQIABAA&oq=crypto+hash+contents&gs_lcp=CgNpbWcQA1Cq5QpY9fEKYIj0CmgBcAB4AIAB7AGIAf4GkgEFNC4xLjKYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=CikaYJL8IpG2sAWD1aCACA#imgrc=ajBMH7jMnjAB0M
# https://www.freecodecamp.org/news/create-cryptocurrency-using-python/
# https://hackernoon.com/learn-blockchains-by-building-one-117428612f46
# https://en.wikipedia.org/wiki/Public-key_cryptography
# https://michaelnielsen.org/ddi/how-the-bitcoin-protocol-actually-works/
# https://www.youtube.com/watch?v=bBC-nXj3Ng4


# use scrypt hash algorithm https://en.wikipedia.org/wiki/Scrypt
# use https://en.wikipedia.org/wiki/Merkle_tree
