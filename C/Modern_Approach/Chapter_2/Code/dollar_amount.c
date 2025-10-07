#include <stdio.h>

int main(void){

int amount, remainder,current_amount;

printf("enter a dollar amount:");
scanf("%d", &amount);


/*remainder calc, set & update*/

remainder = amount/20;
printf("$20 bill: %d \n",remainder);
current_amount = amount -(remainder*20);

remainder = current_amount/10;
printf("$10 bill: %d \n",remainder);
current_amount = current_amount -(remainder*10);

remainder = current_amount/5;
printf("$5 bill: %d \n",remainder);
current_amount = current_amount -(remainder*5);


remainder = current_amount/1;
printf("$1 bill: %d \n",remainder);

}