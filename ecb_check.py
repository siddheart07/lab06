# Lab 06 - check for ECB
from collections import Counter

data = open("aes.bmp.enc", "rb").read()
blocks = [data[i:i+16] for i in range(0, len(data) - 15, 16)]
counts = Counter(blocks)

print("file size:", len(data), "bytes")
print("total 16-byte blocks:", len(blocks))
print("unique blocks:", len(counts))
print()
print("most repeated blocks:")
for block, n in counts.most_common(5):
    print(block.hex(), "->", n, "times")
