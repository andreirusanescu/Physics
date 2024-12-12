import matplotlib.pyplot as plt

F = 120
tf = 600
f = 0.2
sigma_f = (f / tf) ** (1 / 2)

print(f"Standard deviation {sigma_f}")

E = [5.48, 21.56, 47.34, 81.56, 122.83, 169.90, 221.63, 277.11, 335.61,
     396.54, 459.44, 523.95, 589.79, 656.74, 724.62, 793.27, 862.59, 932.48]

N_impulses = [464, 558, 831, 1251, 1636, 2089, 2407, 2472, 2511, 2284, 1974, 1692, 1525, 1228, 1030, 772, 660, 563]
t = 120 # seconds

N_impulses_size = len(N_impulses)
n = [0] * N_impulses_size
r = [0] * N_impulses_size
sigma_r = [0] * N_impulses_size

for i in range(N_impulses_size):
    n[i] = N_impulses[i] / t
    r[i] = n[i] - f
    sigma_r[i] = (n[i]/t + f/tf) ** (1 / 2)

print("Impulsuri pe secunda n: ")
for i in range(N_impulses_size):
    print(f"{n[i]:.2}", end=" ")
print()

print("r: ")
for i in range(N_impulses_size):
    print(f"{r[i]:.2}", end=" ")
print()

print("Deviatia standard: ")
for i in range(N_impulses_size):
    print(f"{sigma_r[i]:.2}", end=" ")
print()

E_h = 337
E_max = 3 * E_h 

plt.show()
plt.plot(E, n, 'o-', color='blue', label='n = f(E)')
plt.xlabel('E (keV)')
plt.ylabel('n (imp/s)')
plt.title("Impulsuri in functie de energia cinetica a particulei beta")
plt.legend()
plt.show()
