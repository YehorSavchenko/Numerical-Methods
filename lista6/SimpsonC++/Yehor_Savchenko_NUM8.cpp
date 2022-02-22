#include <iostream>
#include <math.h>

using namespace std;

double function2_logarithm(double x, void *parametr)
{
    double y = *(double *)parametr;
    return log(x * x + y * y * y + 1);
}

double function1_sinus(double x, void *parametr)
{
    return sin(x);
}

double trapezoid(double a, double b, double N, double (*function)(double, void *), void *parametr)
{
    double delta = (b - a) / N;
    double integral = 0.0;
    for (int i = 0; i <= N; i++)
    {
        double x = a + i * delta;
        integral = integral + function(x, parametr);
    }
    double result = delta * (integral - (function(a, parametr) + function(b, parametr)) / 2);
    return result;
}

double romberg(double a, double b, double tolerancja, double (*function)(double, void *), void *parametr)
{
    int index_itr = 1;
    double table[10][10];
    table[0][0] = trapezoid(a, b, pow(2, 0), function, parametr);
    while (true)
    {
        table[index_itr][0] = trapezoid(a, b, pow(2, index_itr), function, parametr);
        for (int i = 1; i <= index_itr; i++)
        {
            table[index_itr][i] = (pow(4, i) * table[index_itr][i - 1] - table[index_itr - 1][i - 1]) / (pow(4, i) - 1);
        }
        if (fabs(table[index_itr][index_itr] - table[index_itr - 1][index_itr - 1]) < tolerancja)
        {
            break;
        }
        index_itr++;
    }
    return table[index_itr][index_itr];
}

double newtonaCotesa(double a, double b, double tolerancja, double (*function)(double, void *), void *parametr)
{
    double integral = tolerancja + 1, new_integral = 0.0;
    for (int N = 2; (N <= 4) || (fabs(new_integral - integral) > tolerancja); N *= 2)
    {
        double delta, sum2 = 0.0, sum4 = 0.0, sum = 0.0;
        delta = (b - a) / (2 * N);
        for (int i = 1; i <= 2 * N - 1; i += 2)
        {
            sum4 += function(a + delta * i, parametr);       //Nieparzyste wartości indeksowane należy pomnożyć przez 4.
            sum2 += function(a + delta * (i + 1), parametr); //Parzyste wartości indeksowane należy pomnożyć przez 2.
        }
        sum = function(a, parametr) + 4 * sum4 + 2 * sum2 - function(b, parametr);
        integral = new_integral;
        new_integral = (delta / 3) * sum;
    }
    return new_integral;
}

double romberg_main_function(double y, void *pr)
{
    return romberg(0, 1, pow(10, -10), function2_logarithm, &y);
}

double simpson_main_function(double y, void *pr)
{
    return newtonaCotesa(0, 1, pow(10, -10), function2_logarithm, &y);
}

int main()
{
    double newtonaCotesa_sinus = newtonaCotesa(0, 1, pow(10, -10), function1_sinus, 0);
    double newtonaCotesa_double = newtonaCotesa(0, 1, pow(10, -10), simpson_main_function, 0);
    double romberga_sinus = romberg(0, 1, pow(10, -10), function1_sinus, 0);
    double romberga_double = romberg(0, 1, pow(10, -10), romberg_main_function, 0);

    printf("Newtona-Cotesa function(sin(x))  =  %.10f\n", newtonaCotesa_sinus);
    printf("Newtona-Cotesa double integral  =  %.10f\n", newtonaCotesa_double);
    printf("Romberg function(sin(x))  =  %.10f\n", romberga_sinus);
    printf("Romberg double integral  =  %.10f\n", romberga_double);
    return 0;
}