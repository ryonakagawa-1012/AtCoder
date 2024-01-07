#include <math.h>
#include <stdio.h>

int main() {
    int A, B;

    scanf("%d,", &A);
    scanf("%d", &B);

    printf("%0.0f", pow(A, B) + pow(B, A));
    return 0;
}