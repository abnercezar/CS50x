#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int main(void)
{
    // Recebe texto
    string texto = get_string("Texto: ");

    // Contagem de Letras
    int qtdletras = 0;
    for (int i = 0; i < strlen(texto); i++)
    {
        if ((texto[i] >= 'a' && texto[i] <= 'z') || (texto[i] >= 'A' && texto[i] <= 'Z'))
            qtdletras++;
    }

    // Contagem de palavras
    int qtdpalavras = 1;
    for (int i = 0; i < strlen(texto); i++)
    {
        if (texto[i] == ' ')
            qtdpalavras++;
    }

    // Contagem de frases
    int qtdfrases = 0;
    for (int i = 0; i < strlen(texto); i++)
    {
        if (texto[i] == '.' || texto[i] == '!' || texto[i] == '?')
            qtdfrases++;
    }

    // Indíce de Coleman-Liau
    float contar = (0.0588 * qtdletras / qtdpalavras * 100) - (0.296 * qtdfrases / qtdpalavras * 100) - 15.8;
    int index = round(contar);

    if (index < 1)
    {
        // Imprimir
        printf("Before Grade 1\n");
        return 0;
    }
    else if (index >= 16)
    {
        // Imprimir
        printf("Grade 16+\n");
        return 0;
    }
    else
    {
        // Imprimir
        printf("Grade %i\n", index);
    }
}