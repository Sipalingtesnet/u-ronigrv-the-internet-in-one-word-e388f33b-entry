"""
Verification script for 'The Internet in One Word' entry.
Verifies determinism, sha256 stability, character length (1-30), single word, UTF-8, and lack of trailing newline.
"""

import subprocess
import hashlib
import os

def run_test():
    # Run main.py twice
    subprocess.run(["python3", "main.py"], check=True)
    with open("/output/entry.txt", "rb") as f:
        content1 = f.read()
    hash1 = hashlib.sha256(content1).hexdigest()

    subprocess.run(["python3", "main.py"], check=True)
    with open("/output/entry.txt", "rb") as f:
        content2 = f.read()
    hash2 = hashlib.sha256(content2).hexdigest()

    # Decode UTF-8
    text = content1.decode("utf-8")

    # Checks
    assert hash1 == hash2, "Hashes do not match between runs!"
    assert 1 <= len(text) <= 30, f"Length {len(text)} out of bounds (1-30)."
    assert not any(c.isspace() for c in text), "Word contains whitespace or spaces!"
    assert text.isalpha(), "Word must contain letters only!"
    assert not text.endswith("\n"), "File contains trailing newline!"

    print("Match: True")

if __name__ == "__main__":
    run_test()
