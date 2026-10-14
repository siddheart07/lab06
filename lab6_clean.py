# Lab 06 - clean ECB block-pattern visualisation
import struct
from collections import Counter

data = open("aes.bmp.enc", "rb").read()
blocks = [data[i:i+16] for i in range(0, len(data), 16)]

background = Counter(blocks).most_common(1)[0][0]
print("background block:", background.hex())

new = b""
for b in blocks:
    if b == background:
        new += b"\xff" * len(b)
    else:
        new += b"\x00" * len(b)

pixels = new[54:]
width = 640
height = 480

header = b"BM"
header += struct.pack("<IHHI", 54 + len(pixels), 0, 0, 54)
header += struct.pack("<IiiHHIIiiII", 40, width, height, 1, 24, 0,
                      len(pixels), 2835, 2835, 0, 0)

open("clean.bmp", "wb").write(header + pixels)
print("saved clean.bmp")
