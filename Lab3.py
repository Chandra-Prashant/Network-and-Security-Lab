SIZE = 7
CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_ "

def create_matrix(key):
    key = key.upper()
    result = ""
    for group in range(3):
        # Match characters from key
        for ch in key:
            if ch in CHARACTERS and ch not in result:
                if (group == 0 and ch.isalpha()) or \
                   (group == 1 and ch.isdigit()) or \
                   (group == 2 and not ch.isalnum()):
                    result += ch
        # Step B: Match remaining characters from CHARACTERS
        for ch in CHARACTERS:
            if ch not in result:
                if (group == 0 and ch.isalpha()) or \
                   (group == 1 and ch.isdigit()) or \
                   (group == 2 and not ch.isalnum()):
                    result += ch
    matrix = []
    for i in range(0, 49, SIZE):
        row = []
        for j in range(SIZE):
            row.append(result[i + j])
        matrix.append(row)
    return matrix

def display_matrix(matrix):
    for row in matrix:
        print(" ".join(row))

def flip_matrix(matrix, key):
    # ASCII sum
    ascii_sum = 0
    for ch in key:
        ascii_sum += ord(ch)
    print("\nASCII Sum of Key:", ascii_sum)
    # Even sum then left to right
    if ascii_sum % 2 == 0:
        print("Even ASCII sum then Matrix flipped Left to Right")
        for i in range(SIZE):
            for j in range(SIZE // 2):
                matrix[i][j], matrix[i][SIZE - 1 - j] = matrix[i][SIZE - 1 - j], matrix[i][j]
    # Odd sum then top to bottom
    else:
        print("Odd ASCII sum then Matrix flipped Top to Bottom")
        for i in range(SIZE // 2):
            for j in range(SIZE):
                matrix[i][j], matrix[SIZE - 1 - i][j] = matrix[SIZE - 1 - i][j], matrix[i][j]
    return matrix

def find_position(matrix, ch):
    for r in range(SIZE):
        for c in range(SIZE):
            if matrix[r][c] == ch:
                return r, c
    return None

def prepare_text(text, filler="X"):
    text = text.upper()
    # Keep only valid characters
    clean_text = ""
    for ch in text:
        if ch in CHARACTERS:
            clean_text += ch
    # Form digraphs
    result = ""
    i = 0
    while i < len(clean_text):
        first = clean_text[i]
        if i + 1 == len(clean_text):
            result += first + filler
            i += 1
        else:
            second = clean_text[i + 1]
            if first == second:
                result += first + filler
                i += 1
            else:
                result += first + second
                i += 2
    return result

def encrypt(plaintext, matrix):
    prepared = prepare_text(plaintext)
    ciphertext = ""
    for i in range(0, len(prepared), 2):
        first = prepared[i]
        second = prepared[i + 1]
        r1, c1 = find_position(matrix, first)
        r2, c2 = find_position(matrix, second)
        # Same row
        if r1 == r2:
            ciphertext += matrix[r1][(c1 + 1) % SIZE]
            ciphertext += matrix[r2][(c2 + 1) % SIZE]
        # Same column
        elif c1 == c2:
            ciphertext += matrix[(r1 + 1) % SIZE][c1]
            ciphertext += matrix[(r2 + 1) % SIZE][c2]
        # Rectangle swap
        else:
            ciphertext += matrix[r1][c2]
            ciphertext += matrix[r2][c1]
    return ciphertext


def decrypt(ciphertext, matrix):
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        first = ciphertext[i]
        second = ciphertext[i + 1]
        r1, c1 = find_position(matrix, first)
        r2, c2 = find_position(matrix, second)
        # Same row
        if r1 == r2:
            plaintext += matrix[r1][(c1 - 1) % SIZE]
            plaintext += matrix[r2][(c2 - 1) % SIZE]
        # Same column
        elif c1 == c2:
            plaintext += matrix[(r1 - 1) % SIZE][c1]
            plaintext += matrix[(r2 - 1) % SIZE][c2]
        # Rectangle swap
        else:
            plaintext += matrix[r1][c2]
            plaintext += matrix[r2][c1]
    return plaintext

key = input("Enter key: ")
plaintext = input("Enter plaintext: ")
matrix = create_matrix(key)
print("\n--- Initial 7x7 Matrix ---")
display_matrix(matrix)
matrix = flip_matrix(matrix, key)
print("\nTransformed Matrix (Used for Cipher)")
display_matrix(matrix)
prepared = prepare_text(plaintext)
ciphertext = encrypt(plaintext, matrix)
decrypted = decrypt(ciphertext, matrix)
print("\nOutput")
print("Prepared Plaintext :", prepared)
print("Ciphertext         :", ciphertext)
print("Decrypted Text     :", decrypted)