#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/aes.h>
#include <openssl/evp.h>
#include <openssl/rand.h>

#define KEY_SIZE 32
#define BLOCK_SIZE 16

int main(int argc, char *argv[]) {
    // Verificar si se proporcionó el archivo a encriptar
    if (argc != 2) {
        printf("Uso: %s <archivo_a_encriptar>\n", argv[0]);
        return 1;
    }

    // Abrir el archivo a encriptar
    FILE *file = fopen(argv[1], "r");
    if (!file) {
        printf("Error al abrir el archivo\n");
        return 1;
    }

    // Leer el contenido del archivo
    fseek(file, 0, SEEK_END);
    long size = ftell(file);
    rewind(file);
    char *content = malloc(size + 1);
    fread(content, 1, size, file);
    content[size] = '\0';

    // Generar una clave aleatoria
    unsigned char key[KEY_SIZE];
    RAND_priv_bytes(key, KEY_SIZE);

    // Inicializar el contexto de cifrado
    EVP_CIPHER_CTX *ctx;
    ctx = EVP_CIPHER_CTX_new();
    EVP_EncryptInit_ex(ctx, EVP_aes_256_cbc(), NULL, key, NULL);

    // Encriptar el contenido
    unsigned char *encrypted = malloc(size + BLOCK_SIZE);
    int len;
    EVP_EncryptUpdate(ctx, encrypted, &len, (unsigned char *)content, size);
    EVP_EncryptFinal_ex(ctx, encrypted + len, &len);

    // Guardar el contenido encriptado en un archivo
    FILE *encrypted_file = fopen("encrypted.txt", "w");
    if (!encrypted_file) {
        printf("Error al abrir el archivo de salida\n");
        return 1;
    }
    fwrite(encrypted, 1, size + BLOCK_SIZE, encrypted_file);
    fclose(encrypted_file);

    // Liberar recursos
    free(content);
    free(encrypted);
    EVP_CIPHER_CTX_free(ctx);
    fclose(file);

    return 0;
}