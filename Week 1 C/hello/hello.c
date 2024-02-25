#include <stdio.h>
#include <cs50.h>
int main(void)
{
    string name = get_string("Qual é o seu nome? ");
    printf("Olá, %s\n", name);
}