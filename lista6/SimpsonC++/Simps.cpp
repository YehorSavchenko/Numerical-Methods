#include <iostream>
#include <math.h>
using namespace std;

double function2_logarithm(double x, void *params)
{
    double y = *(double *)params;
    return log(x * x + y * y * y + 1);
}

double function1_sinus(double x, void *params)
{
    //double y = *(double *) params;
    return sin(x);
}

double integrateNC(double a, double b, double (*f)(double, void *), double eps, void *params)
{
    int N = 2;
    double integral = 0;
    double newIntegral = 1 + eps;
    while (abs(newIntegral - integral) > eps)
    {
        double sumParzyst = 0;
        double sumNieParzyst = 0;
        double WIDTH = (b - a) / N;
        integral = newIntegral;
        for (int i = 0; i < N; i += 2)
        {
            double x = a + WIDTH * i;
            sumParzyst += f(x, params);
            if (i < N - 1)
            {
                double x1 = a + WIDTH * (i + 1);
                sumNieParzyst += f(x1, params);
            }
        }
        newIntegral = (1 / 3) * WIDTH * (f(a, params) + f(b, params) + 2 * sumParzyst + 4 * sumNieParzyst);
        N *= 2;
    }
    return newIntegral;
}

double simps(double a, double b, double (*f)(double, void *), double eps, void *params)
{
    double I = eps + 1, I1 = 0; //I-предыдущее вычисленное значение интеграла, I1-новое, с большим N.
    for (int N = 2; (N <= 4) || (fabs(I1 - I) > eps); N *= 2)
    // for (int N = 2; (fabs(I1 - I) > eps); N *= 4)
    {
        double h, sum2 = 0, sum4 = 0, sum = 0;
        h = (b - a) / (2 * N); //Шаг интегрирования.
        for (int i = 1; i <= 2 * N - 1; i += 2)
        {
            sum4 += f(a + h * i, params);       //Значения с нечётными индексами, которые нужно умножить на 4.
            sum2 += f(a + h * (i + 1), params); //Значения с чётными индексами, которые нужно умножить на 2.
        }
        sum = f(a, params) + 4 * sum4 + 2 * sum2 - f(b, params); //Отнимаем значение f(b) так как ранее прибавили его дважды.
        I = I1;
        I1 = (h / 3) * sum;
    }
    return I1;
}

double trapezoid(double a, double b, double N, double (*f)(double, void *), void *params)
{
    double WIDTH = (b - a) / N;
    double integral = 0.0;

    for (int i = 0; i < N; i++)
    {
        double x = a + (i * WIDTH);
        integral += f(x, params);
    }
    integral = (integral + (1 / 2) * (f(a, params) + f(b, params))) * WIDTH;
    return integral;
}

// double integrateRomberg(double a, double b, double (*f)(double, void *), double eps, void *params)
// {
//     double tablica[30][30];
//     tablica[0][0] = (b - a) / (2 * (f(b, params) + f(a, params)));
//     int iterationNum = 1;
//     while (fabs(tablica[iterationNum - 1][iterationNum - 1] - tablica[iterationNum - 2][iterationNum - 2]) > eps)
//     {
//         tablica[0][iterationNum] = trapezoid(a, b, pow(2, iterationNum), f, params);
//         for (int i = 1; i < iterationNum + 1; i++)
//         {
//             tablica[i][iterationNum] = (pow(4, iterationNum) * tablica[i - 1][iterationNum] - tablica[i - 1][iterationNum - 1]) / (pow(4, iterationNum) - 1);
//         }
//         iterationNum += 1;
//     }
//     return tablica[iterationNum - 1][iterationNum - 1];
// }

double romberg(double a, double b, double (*f)(double, void *), double eps, void *pr)
{
    double tablica[20][20];
    tablica[0][0] = trapezoid(a, b, pow(2, 0), f, pr);
    int iterationNum = 1;
    while (true)
    {
        tablica[iterationNum][0] = trapezoid(a, b, pow(2, iterationNum), f, pr);
        // cout<<"N = "<<iterationNum<<endl;
        for (int i = 1; i <= iterationNum; i++)
        {
            tablica[iterationNum][i] = (pow(4, i) * tablica[iterationNum][i - 1] - tablica[iterationNum - 1][i - 1]) / (pow(4, i) - 1);
        }
        // printf("%.10f\n", tablica[iterationNum][iterationNum]);
        if (fabs(tablica[iterationNum][iterationNum] - tablica[iterationNum - 1][iterationNum - 1]) < eps)
        {
            // cout<<"Liczba iteracji = "<<iterationNum<<endl;
            break;
        }
        iterationNum += 1;
    }
    return tablica[iterationNum][iterationNum];
}

double simpson_main_function(double y, void *params)
{
    return simps(0, 1, function2_logarithm, pow(10, -10), &y);
}

double g_romberga(double y, void *params)
{
    return romberg(0, 1, function2_logarithm, pow(10, -10), &y);
}

// def integrateRomberg(a, b, f, eps):
//     tablica = np.zeros((30, 30))
//     tablica[0][0] = (b-a)/2*(f(b)+f(a))
//     iterationNum = 1
//     while abs(tablica[iterationNum-1][iterationNum-1]-tablica[iterationNum-2][iterationNum-2]) > eps:
//         # print(iterationNum)
//         tablica[0][iterationNum] = trapezoid(a, b, pow(2, iterationNum), f)
//         for i in range(1, iterationNum+1, 1):
//             tablica[i][iterationNum] = (pow(4, iterationNum)*tablica[i-1][iterationNum]-tablica[i-1][iterationNum-1])/(pow(4, iterationNum)-1)
//         iterationNum += 1
//     return tablica[iterationNum-1][iterationNum-1]

int main()
{
    double resultNC = simps(0, 1, simpson_main_function, pow(10, -10), 0);
    double resultNC2 = simps(0, 1, function1_sinus, pow(10, -10), 0);
    double resultNC3 = romberg(0, 1, g_romberga, pow(10, -10), 0);
    cout << "Zarabotaj pozalujsta\n";
    printf("%.10f", resultNC);
    cout << "\nZarabotaj pozalujsta\n";
    printf("%.10f", resultNC2);
    cout << "\nZarabotaj pozalujsta\n";
    printf("%.10f", resultNC3);
    return 0;
}