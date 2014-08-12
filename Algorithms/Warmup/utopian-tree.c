#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int cases = -1;
    int i = 0;
    int j = 0;
    scanf("%d", &cases);
    for(i = 0; i < cases; i ++) {
        int cycles = -1;
        int height = 1;
        scanf("%d", &cycles);
        while(cycles > 0){
            height = height *2;
            cycles--;
            if(cycles > 0) {
                height++;
                cycles--;
            }
        }
        printf("%d\n", height);
    }
    return 0;
}