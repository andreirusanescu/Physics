import numpy as np
import matplotlib.pyplot as plt
import statistics


lambda_Hg = np.array([0.6234, 0.6123, 0.579, 0.577, 0.5461, 0.5025, 0.4358, 0.4347, 0.4339, 0.4078, 0.4047])
x_Hg = np.array([9.5, 10.1, 12.7, 13.1, 15.4, 16.7, 28.2, 29.7, 30, 34, 34.6])
y_Hg = 1 / (lambda_Hg ** 2)

print("Y_HG")
for n in y_Hg:
    print(n, end=" ")
print("")

plt.plot(x_Hg, y_Hg, '*b', label='Hg exp')
plt.xlabel('x (mm)')
plt.ylabel('y (µm^(-2))')
plt.title('Dreapta de Etalonare')

x_interp = np.arange(0, 51, 1)
coef = np.polyfit(x_Hg, y_Hg, 1)
y_interp = np.polyval(coef, x_interp)
plt.plot(x_interp, y_interp, '-r', label='Dreapta de etalonare')

x_H = np.array([6.8, 21.6, 29.9, 33.7, 36.6, 41.1])
y_H = np.polyval(coef, x_H)
plt.plot(x_H, y_H, 'og', label='H exp')

lambda_H = np.sqrt(1 / y_H) * 1000

R_H = []
R_H.append(1 / ((lambda_H[0] * (10 ** (-2))) * (1 / 4 - 1 / 9)))
R_H.append(1 / ((lambda_H[1] * (10 ** (-2))) * (1 / 4 - 1 / 16)))
R_H.append(1 / ((lambda_H[2] * (10 ** (-2))) * (1 / 4 - 1 / 25)))
R_H.append(1 / ((lambda_H[3] * (10 ** (-2))) * (1 / 4 - 1 / 36)))
R_H.append(1 / ((lambda_H[4] * (10 ** (-2))) * (1 / 4 - 1 / 49)))
R_H.append(1 / ((lambda_H[5] * (10 ** (-2))) * (1 / 4 - 1 / 64)))

print(lambda_H)
print(R_H)

R_H_AVG =statistics.mean(R_H)
print(f"{R_H_AVG}")

standard_deviation = 0
for i in range(1, 7):
    standard_deviation += ((R_H[i - 1] - R_H_AVG) ** 2)
standard_deviation = (standard_deviation / 30) ** (1 / 2)


print(standard_deviation)


plt.legend()
plt.show()
plt.plot(x_Hg, lambda_Hg, '*b', label='Hg exp')
plt.xlabel('x (mm)')
plt.ylabel('lambda Hg (nm)')
plt.title('Curba de Etalonare')

plt.legend()
plt.show()
