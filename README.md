# Lab 06 – Encrypted Image (AES-ECB)

**Module:** Secure Communication and Cryptography  
**Challenge:** Lab 06 – Encrypted Image  
**Team:** Ram Siddharth R R and Jeyanth Kannan  
**Result:** `Tro11d`

## Aim

The supplied bitmap was encrypted using AES in ECB mode. The aim was not to recover the AES key, but to show that ECB leaks repeated image patterns because identical plaintext blocks produce identical ciphertext blocks.

## Method

1. Inspect the supplied `aes.bmp.enc` file.
2. Count repeated 16-byte blocks using `ecb_check.py`.
3. Use the file size to identify a 640 × 480, 24-bit BMP layout.
4. Rebuild a valid BMP header with `lab6_fix.py`.
5. Create a black/white ECB-pattern visualisation with `lab6_clean.py`.
6. Compare ECB and CBC using `ecb_vs_cbc.sh`.

## Block statistics

- File size: **921,654 bytes**
- Complete 16-byte blocks: **57,603**
- Unique blocks: **1,076**
- Most common block: **51,221 occurrences**

## Image-size calculation

```text
921,654 - 54 = 921,600 bytes
921,600 / 3 = 307,200 pixels
640 × 480 = 307,200 pixels
```

This is consistent with a **640 × 480, 24-bit BMP**.

## Result

After rebuilding the BMP header, the encrypted pixel data still showed ECB stripe patterns and the hidden text `Tro11d`. Mapping the most common ciphertext block to white and the other blocks to black made the text clearer.

## Security lesson

The AES key was not recovered and AES itself was not broken. The weakness comes from ECB mode because repeated plaintext blocks remain visible as repeated ciphertext patterns. An authenticated mode such as **AES-GCM** is a safer choice for modern systems.

## Run

Place `aes.bmp.enc` in this folder and run:

```bash
python3 ecb_check.py
python3 lab6_fix.py
python3 lab6_clean.py
bash ecb_vs_cbc.sh
```

The challenge ciphertext is not included unless redistribution is permitted by the lecturer.
