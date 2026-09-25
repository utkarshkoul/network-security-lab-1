import hashlib
import hmac
import secrets
import time

SHARED_SECRET = b"network_security_lab_secret"
MAX_AGE_SECONDS = 5
SEEN_NONCES = set()


def generate_challenge(username):
    nonce = secrets.token_hex(16)
    timestamp = int(time.time())
    message = f"{username}:{nonce}:{timestamp}".encode("utf-8")
    tag = hmac.new(SHARED_SECRET, message, hashlib.sha256).hexdigest()
    return {
        "username": username,
        "nonce": nonce,
        "timestamp": timestamp,
        "tag": tag,
    }


def verify_response(response):
    username = response.get("username")
    nonce = response.get("nonce")
    timestamp = response.get("timestamp")
    tag = response.get("tag")

    if not all([username, nonce, timestamp, tag]):
        return "Rejected: Missing required authentication fields."

    if nonce in SEEN_NONCES:
        return "Rejected: Replay attack detected (nonce already used)."

    if abs(time.time() - int(timestamp)) > MAX_AGE_SECONDS:
        return "Rejected: Expired challenge response."

    message = f"{username}:{nonce}:{timestamp}".encode("utf-8")
    expected_tag = hmac.new(SHARED_SECRET, message, hashlib.sha256).hexdigest()

    if not hmac.compare_digest(expected_tag, tag):
        return "Rejected: Tampered HMAC tag."

    SEEN_NONCES.add(nonce)
    return f"Accepted: Valid challenge-response for {username}."


def main():
    print("=== Challenge-Response Authentication Simulation ===")

    valid_response = generate_challenge("alice")
    print("\n1. Valid challenge generated:", valid_response)
    print("Result:", verify_response(valid_response))

    replay_response = valid_response.copy()
    print("\n2. Replayed nonce check:")
    print("Result:", verify_response(replay_response))

    expired_response = generate_challenge("alice")
    expired_response["timestamp"] = int(time.time()) - 20
    print("\n3. Expired timestamp check:")
    print("Result:", verify_response(expired_response))

    tampered_response = generate_challenge("alice")
    tampered_response["tag"] = "00" + tampered_response["tag"][2:]
    print("\n4. Tampered HMAC check:")
    print("Result:", verify_response(tampered_response))


if __name__ == "__main__":
    main()
