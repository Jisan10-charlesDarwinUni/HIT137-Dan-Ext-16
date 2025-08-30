#!/usr/bin/env python3
from pathlib import Path

def encrypt_text(plain: str, shift1: int, shift2: int) -> str:
    out = []
    for ch in plain:
        if 'a' <= ch <= 'm':
            base = ord('a')
            shift = shift1 * shift2
            out.append(chr(((ord(ch) - base + shift) % 13) + base))
        elif 'n' <= ch <= 'z':
            base = ord('n')
            shift = -(shift1 + shift2)
            out.append(chr(((ord(ch) - base + shift) % 13) + base))
        elif 'A' <= ch <= 'M':
            base = ord('A')
            shift = -shift1
            out.append(chr(((ord(ch) - base + shift) % 13) + base))
        elif 'N' <= ch <= 'Z':
            base = ord('N')
            shift = (shift2 ** 2)
            out.append(chr(((ord(ch) - base + shift) % 13) + base))
        else:
            out.append(ch)
    return ''.join(out)

def decrypt_text(cipher: str, shift1: int, shift2: int) -> str:
    out = []
    for ch in cipher:
        if 'a' <= ch <= 'm':
            base = ord('a')
            shift = -(shift1 * shift2)
            out.append(chr(((ord(ch) - base + shift) % 13) + base))
        elif 'n' <= ch <= 'z':
            base = ord('n')
            shift = (shift1 + shift2)
            out.append(chr(((ord(ch) - base + shift) % 13) + base))
        elif 'A' <= ch <= 'M':
            base = ord('A')
            shift = shift1
            out.append(chr(((ord(ch) - base + shift) % 13) + base))
        elif 'N' <= ch <= 'Z':
            base = ord('N')
            shift = -(shift2 ** 2)
            out.append(chr(((ord(ch) - base + shift) % 13) + base))
        else:
            out.append(ch)
    return ''.join(out)

def main():
    shift1 = int(input("Enter shift1: "))
    shift2 = int(input("Enter shift2: "))

    original = Path("raw_text.txt").read_text(encoding="utf-8")

    encrypted = encrypt_text(original, shift1, shift2)
    Path("encrypted_text.txt").write_text(encrypted, encoding="utf-8")

    decrypted = decrypt_text(encrypted, shift1, shift2)
    Path("decrypted_text.txt").write_text(decrypted, encoding="utf-8")

    if original == decrypted:
        print("Verification: SUCCESS (decrypted matches original)")
    else:
        print("Verification: FAIL (decrypted does not match original)")

if __name__ == "__main__":
    main()
