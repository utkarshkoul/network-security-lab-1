# Experiment 3: Challenge-Response Authentication Using HMAC-SHA256

## Aim
To develop a basic challenge-response authentication system to validate user identity and simulate replay attack detection.

## Theory
Challenge-response authentication is a security mechanism in which the system sends a unique challenge to the user, and the user responds with a valid value generated using a shared secret. This ensures that only a legitimate user who knows the secret can produce a correct response.

A nonce is a random value used only once. It makes each challenge unique and prevents replay attacks, where an attacker captures a previously valid response and reuses it. Timestamping is also useful because it ensures that responses are accepted only within a valid time window.

HMAC (Hash-based Message Authentication Code) combines a secret key with a cryptographic hash function to provide message integrity and authenticity. In this experiment, HMAC-SHA256 is used to generate a response tag that proves the message came from someone who knows the shared secret. If the tag is modified, the verification fails.

A replay attack occurs when an attacker captures a valid authentication response and sends it again to gain unauthorized access. By checking whether a nonce has already been used and whether the timestamp is still fresh, the system can identify such attempts.

## Methodology
1. A shared secret key was initialized between the system and the user.
2. A unique challenge was generated using a random 16-byte nonce and the current timestamp.
3. The username, nonce, and timestamp were combined into a message.
4. An HMAC-SHA256 tag was generated using the shared secret.
5. The server stored the nonce and verified the response when it was received.
6. If the nonce was reused, the response was rejected as a replay attack.
7. If the timestamp was older than 5 seconds, the response was rejected as expired.
8. If the HMAC value was altered, the system rejected the response as tampered.
9. The program tested all four cases: valid response, replayed nonce, expired timestamp, and modified HMAC.

## Algorithm
1. Initialize the shared secret key.
2. Generate a random nonce and current timestamp.
3. Create the challenge message using the username, nonce, and timestamp.
4. Compute the HMAC-SHA256 tag using the secret key.
5. Send the username, nonce, timestamp, and tag to the verifier.
6. Check whether the nonce has already been used.
7. Check whether the timestamp is within the allowed time window.
8. Recompute the expected HMAC and compare it with the received HMAC.
9. Accept the response only if all checks pass; otherwise reject it.

## Program File
The complete Python implementation for this experiment is stored separately in the Code folder as a dedicated program file.

> [**View HMAC Code**](Code/HMAC_Challenge_Response.py)
>
![alt text](Outputs/HMAC.png)
> **HMAC Challenge-Response Output**

## Result
The valid challenge-response authentication was accepted successfully. When the same nonce was reused, the system detected a replay attack and rejected the request. When the timestamp was too old, the response was rejected as expired. When the HMAC tag was modified, the system rejected the tampered response.

## Discussion
The experiment shows that a challenge-response system is effective when it uses a unique nonce, a fresh timestamp, and an HMAC tag. The nonce prevents replay attacks by ensuring each challenge is unique. The timestamp limits the validity of the response to a short time period, preventing delayed reuse. The HMAC ensures integrity and authenticity because even a small modification in the message or tag causes verification to fail.

This combination of nonce, time check, and HMAC creates a reliable authentication mechanism for verifying user identity and detecting malicious attempts.

## Improvements
An additional tampering test was added to modify the HMAC value intentionally and verify that the system rejects altered responses. This improvement clearly demonstrates that HMAC protects data from unauthorized modification and confirms the authenticity of the sender.

## Conclusion
The challenge-response authentication experiment was successfully implemented using nonce, timestamp, and HMAC-SHA256. The results demonstrate that the system can authenticate valid users and reject replayed, expired, and tampered responses. This proves that challenge-response authentication with HMAC is an effective method for securing identity verification in a network environment.
