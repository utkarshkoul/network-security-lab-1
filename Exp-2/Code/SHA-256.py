import hashlib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SAMPLE_PATH = BASE_DIR / "sample.txt"


def hash_file(file_path):
    hash_value = hashlib.sha256()
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash_value.update(chunk)
    return hash_value.hexdigest()


def count_different_hex_chars(hash1, hash2):
    return sum(1 for a, b in zip(hash1, hash2) if a != b)


def main():
    original_text = "Network Security is important in it"
    SAMPLE_PATH.write_text(original_text, encoding="utf-8")

    original_hash = hash_file(SAMPLE_PATH)
    print("Original Text:", original_text)
    print("Original SHA-256:", original_hash)
    print("Status before modification: Matched")

    modified_text = original_text.replace("important", "Important", 1)
    SAMPLE_PATH.write_text(modified_text, encoding="utf-8")

    modified_hash = hash_file(SAMPLE_PATH)
    status = "Matched" if original_hash == modified_hash else "Mismatched"

    print("Modified Text:", modified_text)
    print("Modified SHA-256:", modified_hash)
    print("Tamper verification status:", status)
    print("Different hex characters:", count_different_hex_chars(original_hash, modified_hash), "/ 64")

    if status == "Mismatched":
        print("Tampering detected: the file content has changed.")
    else:
        print("File integrity verified: the content matches the trusted hash.")


if __name__ == "__main__":
    main()
