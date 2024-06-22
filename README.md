# Message Encryption in images
## Encryption
1. Last bit of every image pixel is emptied to store the encrypted message.Last bit is used as it has the least impact on the output of the image i.e 2^0==1 magnitude.
2. Text is converted to binary (1 char = 7 bits).
3. Text is encrypted to the image.
3. New image is saved.

## Decryption
1. Read last bit of image pixels.
2. Convert binary to text string.
