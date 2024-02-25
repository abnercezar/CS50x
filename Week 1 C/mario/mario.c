#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    do
    {
        // Digite a Altura
        n = get_int("Altura: ");
    } while (n < 1 || n > 8);

    for (int i = 0; i < n; i++)
    {
        // Espaços
        for (int j = n - i; j > 1; j--)
            printf(" ");

        // Tijolos
        for (int j = 0; j <= i; j++)
            printf("#");

        printf("\n");
    }
}