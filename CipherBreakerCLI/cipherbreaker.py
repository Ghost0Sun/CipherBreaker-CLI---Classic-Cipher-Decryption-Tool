from collections import Counter

ENGLISH_FREQ_ORDER = 'etaoinshrdlucmfwypvbgkjqxz'

def decrypt_caesar(ciphertext, shift):
    decrypted = ""
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted += char
    return decrypted

def brute_force_caesar(ciphertext):
    print("\n🔎 Trying all 25 Caesar shifts:\n")
    for shift in range(1, 26):
        guess = decrypt_caesar(ciphertext, shift)
        if is_probably_english(guess):
            print(f"✅ [Likely Match — Shift {shift}] {guess}")
        else:
            print(f"[Shift {shift}] {guess}")

def decrypt_vigenere(ciphertext, key):
    decrypted = []
    key = key.lower()
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            base = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            decrypted.append(decrypted_char)
            key_index += 1
        else:
            decrypted.append(char)

    return ''.join(decrypted)

def vigenere_prompt():
    cipher = input("\n🔐 Enter Vigenère encrypted text: ")
    key = input("🧩 Enter the key (known): ")
    result = decrypt_vigenere(cipher, key)
    print(f"\n🧠 Decrypted message:\n{result}")

def decrypt_substitution(ciphertext, key_mapping):
    decrypted = []
    for char in ciphertext:
        if char.lower() in key_mapping:
            new_char = key_mapping[char.lower()]
            if char.isupper():
                new_char = new_char.upper()
            decrypted.append(new_char)
        else:
            decrypted.append(char)
    return ''.join(decrypted)

def substitution_prompt():
    cipher = input("\n🕵️ Enter substitution cipher text: ")
    key = guess_substitution_key(cipher)
    decrypted = decrypt_substitution(cipher, key)

    print("\n🧠 Best guess based on frequency analysis:\n")
    print(decrypted)
    print("\n🔑 Key Mapping:")
    for k, v in key.items():
        print(f"{k.upper()} → {v.upper()}")


def guess_substitution_key(ciphertext):
    # Count letter frequency in ciphertext
    letters_only = [c.lower() for c in ciphertext if c.isalpha()]
    freq = Counter(letters_only)
    sorted_letters = [item[0] for item in freq.most_common()]

    # Map top letters in ciphertext to most common English letters
    guessed_key = {}
    for cipher_letter, plain_letter in zip(sorted_letters, ENGLISH_FREQ_ORDER):
        guessed_key[cipher_letter] = plain_letter

    return guessed_key


def is_probably_english(text):
    common_words = ['the', 'this', 'that', 'and', 'have', 'you', 'is', 'in', 'on']
    matches = sum(1 for word in common_words if word in text.lower())
    return matches >= 2


if __name__ == "__main__":
    print("🔐 Welcome to CipherBreaker CLI!")
    print("1. Break Caesar Cipher")
    print("2. Decrypt Vigenère Cipher (with known key)")
    print("3. Crack Substitution Cipher (basic AI)")
    choice = input("Choose an option (1/2/3): ")

    if choice == "1":
        cipher = input("🔐 Enter Caesar encrypted text: ")
        brute_force_caesar(cipher)

    elif choice == "2":
        vigenere_prompt()

    elif choice == "3":
        substitution_prompt()

    else:
        print("❌ Invalid choice.")

