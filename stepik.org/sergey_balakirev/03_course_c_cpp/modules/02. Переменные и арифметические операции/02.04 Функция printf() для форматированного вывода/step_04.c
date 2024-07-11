#include <stdio.h>

int main(void){
    char ch = 'u';
    short sh = -55;
    int var_i = 1024;
    double var_d = 3.1415;

    putchar(ch);
    printf(" %d %d %f", sh, var_i, var_d);
    return 0;
}