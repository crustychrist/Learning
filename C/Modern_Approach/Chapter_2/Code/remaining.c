#include<stdio.h>

int main (void) {

float loan_sum, interest_rate, monthly_payment, payments;

printf("Enter amount of loan: ");
scanf("%f", &loan_sum);

printf("Enter interest rate: ");
scanf("%f", &interest_rate);

printf("Enter monthly payment: ");
scanf("%f", &monthly_payment);

/*calculating payments*/

interest_rate = (interest_rate/100)/12;
payments = loan_sum+(loan_sum*(interest_rate)) - (monthly_payment);
printf("balance remaining after first payment: %.2f \n", payments);

payments = payments+(payments*(interest_rate)) - (monthly_payment);
printf("balance remaining after second payment: %.2f \n", payments);

payments = payments+(payments*(interest_rate)) - (monthly_payment);
printf("balance remaining after third payment: %.2f \n", payments);

return 0;

}