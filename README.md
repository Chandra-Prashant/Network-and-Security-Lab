# Network and Security Lab

Three standalone Python programs implementing classical substitution
ciphers, built as coursework for a Network and Security lab. Each file is
self-contained and runs independently.

## Programs

- **`Lab1.py`** - Monoalphabetic (Caesar) cipher. A menu-driven
  encrypt/decrypt tool with two shift modes: a fixed shift of 3, or a
  dynamic shift equal to the length of the input text (ignoring spaces).
  Encryption and decryption both work mod 26 over `a`-`z`, passing
  non-alphabetic characters through unchanged.

- **`Lab2.py`** - Extended Vigenère cipher with an added bitwise
  transformation step. For each plaintext letter it computes the standard
  Vigenère sum (`plaintext + key`, mod 26 with the key repeating), then
  performs a nibble swap between the resulting ciphertext value and the
  corresponding key value (`(C & 0xF0) | (K & 0x0F)` and the mirror for
  K), re-maps the swapped value back into the A-Z range, and prints a
  full per-character trace (decimal and 8-bit binary) of every
  intermediate value so the transformation is auditable step by step.

- **`Lab3.py`** - A custom 7x7 Playfair-style cipher over a 49-character
  alphabet (A-Z, 0-9, and a symbol set) instead of the classic 5x5
  letters-only grid. The key matrix is built in three passes - letters
  first, then digits, then symbols - deduplicating repeated characters,
  then conditionally flipped (left-right if the key's ASCII sum is even,
  top-to-bottom if odd) before use. Plaintext is prepared into digraphs
  (splitting repeated-letter pairs and padding an odd final character with
  `X`), then encrypted/decrypted with the standard Playfair row/column/
  rectangle rules extended to the 7x7 grid.

## Running

Each script is interactive and self-contained:

```bash
python3 Lab1.py
python3 Lab2.py
python3 Lab3.py
```

No external dependencies - standard library only.
