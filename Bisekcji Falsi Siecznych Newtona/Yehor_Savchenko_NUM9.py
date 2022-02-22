import numpy as np
import matplotlib.pyplot as plt

root_precision = 10 ** (-6)  # dokładność wyznaczenia pierwiastka


def f_a(x):
    return np.sin(x) - 0.37


def f_a_diff(x):
    return np.cos(x)


def f_b(x):
    return (np.sin(x) - 0.37) * (np.sin(x) - 0.37)


def f_b_diff(x):
    return 2 * (np.sin(x) - 0.37) * np.cos(x)


def f_b_opt(x):
    return f_b(x) / f_b_diff(x)


def f_b_opt_diff(x):
    return 0.5 * ((np.sin(x) - 0.37) * np.tan(x) / np.cos(x) + 1)


def bisekcja(a, b, f, itr, dokl):
    y = [[], []]
    punkt_srodkowy = 0
    if f(a) * f(b) > 0:
        itr = 0
        return "Funkcja nie spelnia zalozen", itr, y
    else:
        while np.fabs(a - b) > root_precision:
            y[0].append(np.abs(punkt_srodkowy - dokl))
            y[1].append(itr)
            punkt_srodkowy = (a + b) / 2
            if f(a) * f(punkt_srodkowy) < 0:
                b = punkt_srodkowy
            else:
                a = punkt_srodkowy
            itr += 1

    return punkt_srodkowy, itr, y


def falsi(a, b, f, itr, dokl):
    y = [[], []]
    punkt_srodkowy = 0
    if f(a) * f(b) > 0:
        itr = 0
        return "Funkcja nie spelnia zalozen", itr, y
    else:
        while np.fabs(a - b) > root_precision:
            punkt_srodkowy = a - (f(a) * (b - a)) / (f(b) - f(a))
            y[0].append(np.abs(punkt_srodkowy - dokl))
            y[1].append(itr)
            itr += 1
            if np.fabs(f(punkt_srodkowy)) < root_precision:
                break
            if f(a) * f(b) < 0:
                b = punkt_srodkowy
            else:
                a = punkt_srodkowy
        return punkt_srodkowy, itr, y


def siecznych(a, b, f, itr, dokl):
    y = [[], []]
    punkt_srodkowy = 0
    while np.fabs(a - b) > root_precision:
        y[0].append(np.abs(punkt_srodkowy - dokl))
        punkt_srodkowy = a - f(a) * (a - b) / (f(a) - f(b))
        y[1].append(itr)
        itr += 1
        b = a
        a = punkt_srodkowy
    return punkt_srodkowy, itr, y


def newtona(a, f, fp, itr, dokl):
    y = [[], []]
    punkt_srodkowy = a
    x1 = punkt_srodkowy - 1
    while np.fabs(x1 - punkt_srodkowy) > root_precision:
        y[0].append(np.abs(punkt_srodkowy - dokl))
        y[1].append(itr)
        x1 = punkt_srodkowy
        punkt_srodkowy = punkt_srodkowy - f(punkt_srodkowy) / fp(punkt_srodkowy)
        itr += 1
    return punkt_srodkowy, itr, y


dolny = 0
gorny = np.pi * 0.5
dokladna = np.arcsin(0.37)

# Biceksja
iterator1 = 0
iterator2 = 0
iterator3 = 0
result_f, iterator1, graf1 = bisekcja(dolny, gorny, f_a, iterator1, dokladna)
result_g, iterator2, graf2 = bisekcja(dolny, gorny, f_b, iterator2, dokladna)
print("Biceksja: ")
print("f(x) = ", result_f, " | itr = ", iterator1)
print("g(x) = ", result_g, " | itr = ", iterator2)

# Falsi
iterator1 = 0
iterator2 = 0
result_f, iterator1, graf12 = falsi(dolny, gorny, f_a, iterator1, dokladna)
result_g, iterator2, graf2 = falsi(dolny, gorny, f_b, iterator2, dokladna)
print("Falsi: ")
print("f(x) = ", result_f, " | itr = ", iterator1)
print("g(x) = ", result_g, " | itr = ", iterator2)

# Siecznych
iterator1 = 0
iterator2 = 0
iterator3 = 0
result_f, iterator1, graf13 = siecznych(dolny, gorny, f_a, iterator1, dokladna)
result_g, iterator2, graf21 = siecznych(dolny, gorny, f_b, iterator2, dokladna)
result_g_1, iterator3, graf31 = siecznych(dolny, gorny - 0.1, f_b_opt, iterator3, dokladna)

print("Siecznych: ")
print("f(x) = ", result_f, " | itr = ", iterator1)
print("g(x) = ", result_g, " | itr = ", iterator2)
print("u(x) = ", result_g_1, " | itr = ", iterator3)

# Newtona
iterator1 = 0
iterator2 = 0
iterator3 = 0
result_f, iterator1, graf14 = newtona(dolny, f_a, f_a_diff, iterator1, dokladna)
result_g, iterator2, graf22 = newtona(np.pi / 2 - 1, f_b, f_b_diff, iterator2, dokladna)
result_g_1, iterator3, graf32 = newtona(np.pi / 2 - 1, f_b_opt, f_b_opt_diff, iterator3, dokladna)
print("Newtona: ")
print("f(x) = ", result_f, " | itr = ", iterator1)
print("g(x) = ", result_g, " | itr = ", iterator2)
print("u(x) = ", result_g_1, " | itr = ", iterator3)

# Grafiki
plt.title("Funkcja f(x)")
plt.yscale("log")
plt.grid()
plt.plot(graf1[1], graf1[0], "-o", label="bisekcja")
plt.plot(graf12[1], graf12[0], "-o", label="falsi")
plt.plot(graf13[1], graf13[0], "-o", label="siecznych")
plt.plot(graf14[1], graf14[0], "-o", label="newtona")
plt.legend()
plt.savefig("f(x)")
plt.show()

plt.title("Funkcja g(x)")
plt.yscale("log")
plt.grid()
plt.plot(graf21[1], graf21[0], "-o", label="siecznych")
plt.plot(graf22[1], graf22[0], "-o", label="newtona")
plt.legend()
plt.savefig("g(x)")
plt.show()

plt.title("Funkcja u(x)")
plt.yscale("log")
plt.grid()
plt.plot(graf31[1], graf31[0], "-o", label="siecznych")
plt.plot(graf32[1], graf32[0], "-o", label="newtona")
plt.legend()
plt.savefig("u(x)")
plt.show()

print("Dokładna wartość = ", dokladna)
