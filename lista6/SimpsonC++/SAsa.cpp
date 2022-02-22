#include <iostream>
#include <math.h>
using namespace std;


double function2_logarithm(double x, void *params){
    double y = *(double *) params;
    return log(x*x+y*y*y+1);
}

double integrateNC(double a, double b, double (*f)(double, void*), double eps, void *params){
    int N = 2;
    double integral = 0.0;
    double newIntegral = 1 + eps;
    while(abs(newIntegral-integral)>eps){
        double sumParzyst = 0.0;
        double sumNieParzyst = 0.0;
        double WIDTH = (b-a)/N;
        integral = newIntegral;
        for(int i = 0; i < N; i+=2){
            double x = a + WIDTH*i;
            sumParzyst+=f(x, params);
            if(i<N-1){
                double x1 = a + WIDTH*(i+1);
                sumNieParzyst += f(x1, params);
            }
        }
        newIntegral = WIDTH/3*(f(a,params)+f(b,params)+2*sumParzyst+4*sumNieParzyst);
        cout<<"\n N: "<<N<<endl;
        N*=2;

    }
    return newIntegral;
}
double simpson_main_function(double y, void *params){
    return integrateNC(0, 1, function2_logarithm,pow(10, -10) ,&y);
}



int main(){
    double resultNC = integrateNC(0, 1, simpson_main_function, pow(10, -10), 0);
    cout<<"Zarabotaj pozalujsta\n"<<resultNC<<endl;
    return 0;
}