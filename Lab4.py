MOD=26
dic={'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
       'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17,
       'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
rev_dic={0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
           10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R',
           18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}

plaintext="MEET, ME AT THE MOON!"
k1=[
    [3, 10, 20],
    [20, 9, 17],
    [9, 4, 17]
]
k2=[
    [2, 4, 5],
    [9, 10, 7],
    [3, 6, 8]
]

def mod_inverse(a, m):
    a=a%m
    for x in range(1, m):
        if(a*x)%m==1:
            return x
    return None

def matrix_inverse(matrix, key_name):
    print(f"\n{key_name}")
    a=matrix[0][0]
    b=matrix[0][1]
    c=matrix[0][2]
    d=matrix[1][0]
    e=matrix[1][1]
    f=matrix[1][2]
    g=matrix[2][0]
    h=matrix[2][1]
    i=matrix[2][2]
    det_raw=a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)
    det=det_raw%MOD
    print(f"Raw Determinant:{det_raw}")
    print(f"Determinant mod 26:{det}")
    det_inv=mod_inverse(det, MOD)
    print(f"Modular Inverse of Determinant (D^-1): {det_inv}")
    if det_inv is None:
        print(f"{key_name} has NO modular inverse then stop.")
        return None
    adj=[
        [(e*i-f*h),-(b*i-c*h),(b*f-c*e)],
        [-(d*i-f*g),(a*i-c*g),-(a*f-c*d)],
        [(d*h-e*g),-(a*h-b*g),(a*e-b*d)]
    ]
    print("Adj Matrix:")
    for row in adj:
        print(" ",row)
    inverse=[]
    for row in range(3):
        new_row=[]
        for col in range(3):
            val=(det_inv*adj[row][col])%MOD
            new_row.append(val)
        inverse.append(new_row)
    print(f"Inverse Key Matrix ({key_name}^-1):")
    for row in inverse:
        print(" ", row)
    return inverse

def encrypt(plaintext, key):
    plaintext=plaintext.upper()
    #Store special characters and clean text
    special_chars=[]
    clean_text=""
    for i in range(len(plaintext)):
        char=plaintext[i]
        if char in dic:
            clean_text+=char
        else:
            special_chars.append([i, char])
    print(f"Original Text: '{plaintext}'")
    print(f"Cleaned Text: '{clean_text}'")
    print(f"Punctuations: {special_chars}")
    while len(clean_text)%3!=0:
        clean_text+="X"
    print(f"Trigrams: '{clean_text}'")
    #Block-by-Block Encryption
    ciphertext=""
    print("\nEncrypting Blockwise:")
    for i in range(0, len(clean_text), 3):
        block=clean_text[i:i+3]
        p=[dic[block[0]], dic[block[1]], dic[block[2]]]
        c=[0, 0, 0]
        for r in range(3):
            c[r]=(key[r][0]*p[0]+key[r][1]*p[1]+key[r][2]*p[2])%MOD
        cipher_block=rev_dic[c[0]]+rev_dic[c[1]]+rev_dic[c[2]]
        ciphertext+=cipher_block
        print(f" Block '{block}' - Vector {p} - Cipher Vector {c} - Cipher Block '{cipher_block}'")
    return ciphertext, special_chars


def decrypt(ciphertext, inverse_key, special_chars):
    print("\nNow Decryption:")
    raw_plaintext = ""
    print("Decrypting Blockwise:")
    for i in range(0, len(ciphertext), 3):
        block=ciphertext[i:i+3]
        c=[dic[block[0]], dic[block[1]], dic[block[2]]]
        p=[0, 0, 0]
        for r in range(3):
            p[r]=(inverse_key[r][0]*c[0]+inverse_key[r][1]*c[1]+inverse_key[r][2]*c[2])%MOD
        plain_block=rev_dic[p[0]]+rev_dic[p[1]]+rev_dic[p[2]]
        raw_plaintext+=plain_block
        print(f" Block '{block}' - Vector {c} - Plain Vector {p} - Plain Block '{plain_block}'")
    print(f"Raw Decrypted Text: '{raw_plaintext}'")
    #Re-insert spaces and punctuation
    plaintext_list=list(raw_plaintext)
    for item in special_chars:
        pos=item[0]
        char=item[1]
        if pos<=len(plaintext_list):
            plaintext_list.insert(pos, char)
    final_text="".join(plaintext_list)
    print(f"Restored Final Decrypted Text: '{final_text}'")
    return final_text


print("Plaintext Input:", plaintext)
inv1=matrix_inverse(k1, "K1")
inv2=matrix_inverse(k2, "K2")
valid_key=None
valid_inverse=None
valid_name=""
if inv1 is not None:
    valid_key=k1
    valid_inverse=inv1
    valid_name="K1"
elif inv2 is not None:
    valid_key=k2
    valid_inverse=inv2
    valid_name="K2"
if valid_key is not None:
    print(f"Using {valid_name} only:")
    ciphertext, special_chars=encrypt(plaintext, valid_key)
    print(f"\nFinal Ciphertext: {ciphertext}")
    decrypted_text=decrypt(ciphertext, valid_inverse, special_chars)
else:
    print("\nNo valid key matrix.")