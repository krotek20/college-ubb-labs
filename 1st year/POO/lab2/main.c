#include <stdio.h>
#include <math.h>

/*double power(float x, int n) {
    if (n == 0) return 1;
    if (n == 1) return x;

    double t = power(x, n / 2);
    t *= t;

    if (n % 2 == 0) return t;
    else return x * t;
}

int main()
{
    float x;
    int n;
    printf("X = ");
    scanf("%f", &x);
    printf("N = ");
    scanf("%d", &n);

    printf("x^n = %lf\n", power(x, n));
    return 0;
}*/

double power(float x, int n) {
    if (n == 0) return 1;
    if (n == 1) return x;

    double t = power(pow(x, 2), n / 2); // (X^2)^(n/2) LOL

    if (n % 2 == 0) return t;
    else return x * t;
}

int main() {
    float x;
    int n;

    printf("X = ");
    scanf("%f", &x);
    printf("N = ");
    scanf("%d", &n);

    printf("x^n = %lf\n", power(x, n));
}