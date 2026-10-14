# Lab 06 - rebuild a valid BMP header
import struct

data = open("aes.bmp.enc", "rb").read()
pixels = data[54:]

print("file size:", len(data))
print("minus 54 byte header:", len(pixels))
print("pixels (3 bytes each for 24 bit):", len(pixels) // 3)
print("640 x 480 =", 640 * 480)

width = 640
height = 480

header = b"BM"
header += struct.pack("<IHHI", 54 + len(pixels), 0, 0, 54)
header += struct.pack("<IiiHHIIiiII", 40, width, height, 1, 24, 0,
                      len(pixels), 2835, 2835, 0, 0)

open("fixed.bmp", "wb").write(header + pixels)
print("saved fixed.bmp (640x480, 24 bit)")
