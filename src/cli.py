import os
import argparse

from detector import identify_file
from hash_utils import sha256_hash


def main():
    parser = argparse.ArgumentParser(
        description="BinaryScope - File Type Identification Tool"
    )

    parser.add_argument(
        "file",
        help="Path to the file to analyze"
    )

    args = parser.parse_args()

    filepath = args.file

    if not os.path.exists(filepath):
        print("[-] File does not exist")
        return

    detected_type = identify_file(filepath)
    file_hash = sha256_hash(filepath)

    extension = os.path.splitext(filepath)[1]

    print("\n===================================")
    print("         BinaryScope")
    print("===================================\n")

    print(f"[+] File            : {filepath}")
    print(f"[+] Detected Type   : {detected_type}")
    print(f"[+] Extension       : {extension}")
    print(f"[+] SHA256 Hash     : {file_hash}")

    if detected_type.lower() not in extension.lower():
        print("[!] WARNING: Extension mismatch detected")

    print("\n===================================\n")


if __name__ == "__main__":
    main()
