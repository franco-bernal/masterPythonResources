#include <stdio.h>
#include <openssl/aes.h>
#include <openssl/rand.h>

#define AES_KEYLEN 256
#define AES_BLOCK_SIZE 16

void handleErrors() {
    ERR_print_errors_fp(stderr);
    abort();
}

void aes_decrypt(const unsigned char *infile, unsigned char *outfile, const unsigned char *key, const unsigned char *iv) {
    AES_KEY decryptKey;
    AES_set_decrypt_key(key, AES_KEYLEN, &decryptKey);
    AES_cbc_encrypt(infile, outfile, AES_BLOCK_SIZE, &decryptKey, (unsigned char*)iv, AES_DECRYPT);
}

int main() {
    FILE *inputFile, *outputFile;
    unsigned char key[AES_KEYLEN / 8];
    unsigned char iv[AES_BLOCK_SIZE];

    // Read key and IV (this should match what was used for encryption)
    // Here we assume they are stored separately or shared securely.

    inputFile = fopen("mi_codigo_cifrado.bin", "rb");
    if (inputFile == NULL) {
        perror("Error opening input file");
        return 1;
    }

    outputFile = fopen("mi_codigo_descifrado.py", "wb");
    if (outputFile == NULL) {
        perror("Error opening output file");
        return 1;
    }

    unsigned char buffer[AES_BLOCK_SIZE];
    unsigned char decryptedBuffer[AES_BLOCK_SIZE];

    size_t bytesRead;
    while ((bytesRead = fread(buffer, 1, AES_BLOCK_SIZE, inputFile)) > 0) {
        aes_decrypt(buffer, decryptedBuffer, key, iv);
        fwrite(decryptedBuffer, 1, bytesRead, outputFile);
    }

    fclose(inputFile);
    fclose(outputFile);

    printf("Archivo descifrado exitosamente.\n");
    return 0;
}
