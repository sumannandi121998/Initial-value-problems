#include <stdio.h>
#include <math.h>

float f(float t,float y)
 {
 return y-t*t+1; //y' of the differential equation
 }
int main()
{
 int i;
 float h,t,y,y1,a_e,e_b;
 h=0.2; //stepsize
 t=0; //initial value of t
 y=0.5; //initial value of y
 printf("\n  t\t  y\t    absolute error   error bound\n");
while (t<=2+h)
   {
    y1=(t+1)*(t+1)-0.5*exp(t); //value of y from analytical solution
    a_e=fabs(y-y1); //absolute error in each step
    e_b=fabs(0.1*(0.5*exp(2)-2)*(exp(t)-1)); //error bound in each step
    printf("%0.3f\t%0.3f\t\t%0.3f\t\t%0.3f\n",t,y,a_e,e_b);
    y=y+h*f(t,y); //formula for euler method
    t=t+h;
    }
}
 
