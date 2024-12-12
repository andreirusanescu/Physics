import matplotlib.pyplot as plt

U = [3e3, 3.3e3, 3.6e3, 3.9e3, 4.2e3, 4.5e3, 4.8e3, 5e3]
U_sqrt = [0] * len(U)
for i in range(len(U)):
    U_sqrt[i] = 1 / ((U[i]) ** (1 / 2))
    print(f"{U_sqrt[i]:.3}", end=" ")
print("")

d1 = 2.13e-10
d2 = 1.23e-10
L = 13.5e-2
sarcina = 1.602e-19
m = 9.109e-31
h = 6.625e-34

D1 = [2.96e-2, 2.82e-2, 2.71e-2, 2.59e-2, 2.54e-2, 2.44e-2, 2.32e-2, 2.28e-2]
D2 = [4.96e-2, 4.9e-2, 4.6e-2, 4.39e-2, 4.24e-2, 4.22e-2, 3.98e-2, 3.91e-2]

lambda1exp = [0] * len(U)
lambda2exp = [0] * len(U)
lambdath = [0] * len(U)

ct = h / ((2 * sarcina * m) ** (1 / 2))

for i in range(len(U)):
    lambda1exp[i] = d1 * D1[i] / (2 * L)
    lambda2exp[i] = d2 * D2[i] / (2 * L)
    lambdath[i] = ct / ((U[i]) ** (1 / 2))

    print(f"{lambda1exp[i]:.3} {lambda2exp[i]:.3} {lambdath[i]:.3}")


plt.figure(figsize=(8, 6))
plt.plot(U_sqrt, D1, 'o-', label='D1 vs 1/sqrt(U)', color='blue')
plt.plot(U_sqrt, D2, 'o-', label='D2 vs 1/sqrt(U)', color='red')

plt.xlabel("1/sqrt(U) [1/√V]")
plt.ylabel("D [m]")
plt.title("D = f(1 / sqrt(U))")
plt.legend()
plt.grid(True)
plt.show()

k1d1 = 2 * L  * h / (d1 * ((2 * m * sarcina) ** (1 / 2)))
k2d2 = 2 * L  * h / (d2 * ((2 * m * sarcina) ** (1 / 2)))
d1_prim = 2 * L * h / (k1d1 * ((2 * sarcina * m) ** (1 / 2)))
d2_prim = 2 * L * h / (k2d2 * ((2 * sarcina * m) ** (1 / 2)))

print(f"k1d1: {k1d1:.3}, k2d2: {k2d2:.3}, d1_prim: {d1_prim:.3}, d2_prim: {d2_prim:.3}")
