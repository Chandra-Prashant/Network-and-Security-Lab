def run_extended_vigenere(message: str, secret_key: str) -> str:
    clean_message = "".join(filter(str.isalpha, message.upper()))
    clean_key = "".join(filter(str.isalpha, secret_key.upper()))

    if not clean_message or not clean_key:
        print("Error: Plaintext and Key must contain at least one alphabetic character.")
        return ""

    key_len = len(clean_key)
    encrypted_letters = []

    print(f"\n{'Char':<5} | {'P (val/bin)':<14} | {'K (val/bin)':<14} | {'C (val/bin)':<14} | {'New C (val/bin)':<18} | {'New K (val/bin)':<18} | {'Cipher Letter'}")
    print("-" * 110)

    for idx, letter in enumerate(clean_message):
        # 1. Map values to 0-25
        p_val = ord(letter) - ord('A')
        k_val = ord(clean_key[idx % key_len]) - ord('A')

        # 2. Intermediate Vigenere computation
        c_val = (p_val + k_val) % 26

        # 3. 8-bit binary strings
        p_bits = f"{p_val:08b}"
        k_bits = f"{k_val:08b}"
        c_bits = f"{c_val:08b}"

        # 4. Bitwise Nibble Swap (High nibble: 0xF0, Low nibble: 0x0F)
        swapped_c = (c_val & 0xF0) | (k_val & 0x0F)
        swapped_k = (k_val & 0xF0) | (c_val & 0x0F)

        swapped_c_bits = f"{swapped_c:08b}"
        swapped_k_bits = f"{swapped_k:08b}"

        # 5. Map back into alphabet range (0-25) -> 'A'-'Z'
        final_c_val = swapped_c % 26
        cipher_char = chr(final_c_val + ord('A'))
        encrypted_letters.append(cipher_char)

        # Print
        print(
            f"{letter:<5} | "
            f"{p_val:>2} ({p_bits}) | "
            f"{k_val:>2} ({k_bits}) | "
            f"{c_val:>2} ({c_bits}) | "
            f"{swapped_c:>3} ({swapped_c_bits}) | "
            f"{swapped_k:>3} ({swapped_k_bits}) | "
            f"{cipher_char} (value: {final_c_val})"
        )

    return "".join(encrypted_letters)


if __name__ == "__main__":
    raw_text = input("Enter the plaintext: ")
    raw_key = input("Enter the key: ")

    final_cipher = run_extended_vigenere(raw_text, raw_key)

    print("-" * 110)
    print(f"Final Ciphertext: {final_cipher}")