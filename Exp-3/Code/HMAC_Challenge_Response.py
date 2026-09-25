import hmac
import hashlib
import random

secret = b"network123"

# Server creates a challenge
challenge = str(random.randint(1000, 9999))
print("Server Challenge:", challenge)

# Client creates HMAC response
response = hmac.new(
    secret,
    challenge.encode(),
    hashlib.sha256
).hexdigest()

print("Client Response:", response)

# Server creates expected response
expected = hmac.new(
    secret,
    challenge.encode(),
    hashlib.sha256
).hexdigest()

# Authentication
if hmac.compare_digest(response, expected):
    print("Authentication Successful")
else:
    print("Authentication Failed")
