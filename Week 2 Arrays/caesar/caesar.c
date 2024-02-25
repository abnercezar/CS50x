#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
    // Fazer condição de verificação.
    if (argc !=2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else printf("Succes\n");

    // Chave
    string key = argv[1];

    // Verificando entrada
    for (int i = 0; i <strlen(argv[1]); i++)
    {
        if (!isdigit(argv[1][i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }
    printf("Succes\n%s", key);

    //Texto simples
    string plaintext = get_string("plaintext: ");

    //Converter chave
    int k = atoi(key);
    printf("ciphertext: ");

    //Texto cifrado
    for (int i = 0; i < strlen(plaintext); i++)
    {
        if (isupper(plaintext[i]))
        {
            printf("%c", (((plaintext[i] - 65) + k) % 26) + 65);
        }
        else if (islower(plaintext[i]))
        {
            printf("%c", (((plaintext[i] - 97) + k) % 26) + 97);
        }

        else
        {
            printf("%c", plaintext[i]);
        }
    }

    printf("\n");
}