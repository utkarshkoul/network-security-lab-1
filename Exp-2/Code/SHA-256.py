
import hashlib
import random

secret = "network123"

# Server creates a new challenge
challenge = str(random.randint(100000, 999999))

print("Challenge from Server:", challenge)

# Client creates response
response = hashlib.sha256(
    (secret + challenge).encode()
).hexdigest()

print("Response from Client:", response)

# Server calculates expected response
expected = hashlib.sha256(
    (secret + challenge).encode()
).hexdigest()

# Authentication
if response == expected:
    print("Authentication Successful")
else:
    print("Authentication Failed")
