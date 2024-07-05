#include <stdio.h>

int main(void){
    char first_char;
    char second_char;
    char third_char;

    first_char = getchar();
    second_char = getchar();
    third_char  = getchar();

    putchar(third_char);
    putchar(second_char);
    putchar(first_char);

    return 0;
}