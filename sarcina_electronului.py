import math
import statistics
import matplotlib.pyplot as plt
import numpy as np

n = 130
R = 0.150
u0 = 4 * math.pi * (10 ** (-7))
r = 0.04
U = 140

sarcina_specifica = 1.602 * (10 ** (-19)) / (9.1 * (10 ** (-31)))

print(f"Sarcina specifica este: {sarcina_specifica:.2e}")

sarcini = [1.758e+11, 1.698e+11, 1.742e+11, 1.769e+11, 1.737e+11]
base_I = ((125 / 32) * (R ** 2) * U / ((u0 * n * r) ** 2)) ** (1 / 2)

N = len(sarcini)
I = [0] * N
for i in range(0, N):
    I[i] = base_I / (sarcini[i] ** (1 / 2))
    print(f"{I[i]:.3e}")

I_mediu = statistics.mean(I)
B = (4 / 5) ** (3 / 2) * u0 * n * I_mediu / R

print(f"I mediu este de: {I_mediu:.3e}A")
print(f"B mediu este de valoare: {B:.3e}T")
print(f"Sarcina medie este de {statistics.mean(sarcini):.3e}")

suma = 0
for i in range(0, N):
    suma += (I[i] - I_mediu) ** 2
sigma = math.sqrt(suma / (N * (N - 1)))

print(f"Sigma mediu este: {sigma:.3e}\n")

U_vec = [140, 160, 180, 200, 220, 240, 260]
r_vec = [0.05, 0.04, 0.03]
N_U_vec = len(U_vec)
N_r_vec = len(r_vec)

sarcini = [[0] * N_r_vec for _ in range(N_U_vec)]
sarcini[0] = [1.69e+11, 1.71e+11, 1.70e+11]
sarcini[1] = [1.68e+11, 1.74e+11, 1.77e+11]
sarcini[2] = [1.70e+11, 1.76e+11, 1.78e+11]
sarcini[3] = [1.67e+11, 1.71e+11, 1.77e+11]
sarcini[4] = [1.75e+11, 1.73e+11, 1.72e+11]
sarcini[5] = [1.8e+11, 1.79e+11, 1.8e+11]
sarcini[6] = [1.77e+11, 1.78e+11, 1.77e+11] 
I = [[0] * N_r_vec for _ in range(N_U_vec)]
I_mediu = [0] * N_r_vec

I_squared_4cm = [0] * N_U_vec

for i in range(0, N_U_vec):
    print(f"Pentru tensiunea de: {U_vec[i]}")
    for j in range(0, N_r_vec):
        I[i][j] = ((125 / 32) * (R ** 2) * U_vec[i] / ((u0 * n * r_vec[j]) ** 2 * sarcini[i][j])) ** (1 / 2)
        print(f"{I[i][j]:.3e}", end=" ")
    I_squared_4cm[i] = I[i][1] ** 2
    print("\n")

sarciniile_medii = [0] * N_r_vec
for i in range(0, N_r_vec):
    suma = 0
    for j in range(0, N_U_vec):
        suma += sarcini[j][i]
    sarciniile_medii[i] = suma / N_U_vec
    print(f"Sarcina medie pt {r_vec[i]}m este {sarciniile_medii[i]:.3e}")

I = [2.163, 1.618, 1.287]
r_vec = [0.03, 0.04, 0.05]
inv_r_vec = [1 / r for r in r_vec]

plt.plot(inv_r_vec, I, 'o-', label="I = f(1/r)")
plt.xlabel("1/r (cm^-1)")
plt.ylabel("I (A)")
plt.title("Dependenta liniara I = f(1/r)")
slope, intercept = np.polyfit(inv_r_vec, I, 1)


plt.plot(inv_r_vec, np.array(inv_r_vec) * slope + intercept, 'r--', label='Dreapta de regresie')
plt.legend()
plt.grid()
plt.show()

constanta = (5 ** (3 / 2) / (2 ** (5 / 2))) * (R / (n * u0)) * np.sqrt(220) / slope
print(f"Slope: {slope:.3f}")

sarcina_specifica = constanta ** 2
print(f"Sarcina specifica a electronului calculat din panta este: {sarcina_specifica:.3e} C/kg")

plt.plot(U_vec, I_squared_4cm, 'o-', label="I^2 = f(U)")
plt.xlabel("U (V)")
plt.ylabel("I^2 (A^2)")
plt.title("Dependenta liniara I^2 = f(U)")
slope, intercept = np.polyfit(U_vec, I_squared_4cm, 1)

plt.plot(U_vec, np.array(U_vec) * slope + intercept, 'r--', label='Dreapta de regresie')
plt.legend()
plt.grid()
plt.show()

constanta = (125 / 32) * ((R / (n * u0)) ** 2) * 1 / (0.04 ** 2)
print(f"Slope: {slope:.3f}")
print(slope)
sarcina_specifica = constanta * 1 / slope
print(f"Sarcina: {sarcina_specifica:.3e}")
