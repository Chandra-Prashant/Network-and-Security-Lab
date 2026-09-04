chartonum = {chr(97 + i): i for i in range(26)}
numtochar = {i: chr(97 + i) for i in range(26)}

def encrypt(message, shift):
    encrypted = ""
    for char in message:
        if char in chartonum:
            new_num = (chartonum[char] + shift) % 26
            encrypted += numtochar[new_num]
        else:
            encrypted += char
    return encrypted

def decrypt(ciphertext, shift):
    decrypted = ""
    for char in ciphertext:
        if char in chartonum:
            new_num = (chartonum[char] - shift) % 26
            decrypted += numtochar[new_num]
        else:
            decrypted += char
    return decrypted

def main():
    while True:
        print("\nMONOALPHABETIC CIPHER MENU")
        print("Press 1: Caesar Cipher (Shift = 3)")
        print("Press 2: Dynamic Shift (Shift = Text Length)")
        print("Press 3: Exit")
        
        choice = input("Enter choice (1-3): ").strip()
        if choice == "3":
            print("Exiting")
            break
            
        msg = input("Enter plaintext: ").lower()
        
        if choice == "1":
            shift = 3
        elif choice == "2":
            shift = len(msg.replace(" ", ""))
        else:
            print("Invalid option.")
            continue
            
        cipher = encrypt(msg, shift)
        recovered = decrypt(cipher, shift)
        
        print(f"Shift Value   : {shift}")
        print(f"Ciphertext    : {cipher}")
        print(f"Decrypted Text: {recovered}")

if __name__ == "__main__":
    main()