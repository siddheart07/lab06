#!/bin/bash
# Lab 06 - ECB vs CBC comparison

head -c 54 clean.bmp > header.bin
tail -c +55 clean.bmp > pixels.bin

KEY=000102030405060708090a0b0c0d0e0f
IV=0f0e0d0c0b0a09080706050403020100

openssl enc -aes-128-ecb -nosalt -K $KEY -in pixels.bin -out pixels_ecb.bin
openssl enc -aes-128-cbc -nosalt -K $KEY -iv $IV -in pixels.bin -out pixels_cbc.bin

cat header.bin pixels_ecb.bin > test_ecb.bmp
cat header.bin pixels_cbc.bin > test_cbc.bmp

ls -l test_ecb.bmp test_cbc.bmp
