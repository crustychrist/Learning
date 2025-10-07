#include <stdio.h>
#define TAX 0.05f

int main(void) {

    float amount, amount_tax;

    printf("please enter the amount: ");
    scanf("%f", &amount);

    amount_tax = (TAX*amount)+ amount;

    printf("The totale amount is $ %.2f \n", amount_tax);




    return 0;
}