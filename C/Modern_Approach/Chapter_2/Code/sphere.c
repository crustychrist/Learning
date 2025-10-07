#include <stdio.h>
#define PI 3.141

int main(void) {
    float volume, radius, fraction;

    /* Sphere Volume = v = 4/3 * π * r^3 */

    printf("Please enter your radius: ");
    scanf("%f", &radius);
    
    
    fraction = 4.0f / 3.0f;
    volume = fraction * PI * (radius * radius * radius);  // Correct calculation

    printf(" the volume of the sphere is: %.3f", volume);
    return 0;
}