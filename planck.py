import numpy as np
import matplotlib.pyplot as plt

def standard_deviation(color, average) -> float:
	suma = 0
	N = len(color)
	for i in range(N):
		suma += (color[i] - average) ** 2
	sigma = (suma / (N * (N - 1))) ** (1 / 2)
	return sigma

if __name__ == "__main__":
	yellow = [0.529, 0.537, 0.541, 0.554, 0.564, 0.565, 0.567, 0.558,0.566, 0.567]
	yellow_avg = np.mean(yellow)
	sigma_yellow = standard_deviation(yellow, yellow_avg)
	print(f"{yellow_avg:.3e} +- {sigma_yellow:.3e}")

	green = [0.686, 0.684, 0.685, 0.688, 0.693, 0.687, 0.694, 0.693, 0.684, 0.685]
	green_avg = np.mean(green)
	sigma_green = standard_deviation(green, green_avg)
	print(f"{green_avg:.3e} +- {sigma_green:.3e}")

	blue = [0.988, 0.992, 0.989, 0.990, 0.995, 0.997, 0.999, 1.002, 1.000, 1.006]
	blue_avg = np.mean(blue)
	sigma_blue = standard_deviation(blue, blue_avg)
	print(f"{blue_avg:.3e} +- {sigma_blue:.3e}")

	violet = [0.938, 0.943, 0.952, 0.961, 0.941, 0.968, 0.958, 0.947, 0.961, 0.955]
	violet_avg = np.mean(violet)
	sigma_violet = standard_deviation(violet, violet_avg)
	print(f"{violet_avg:.3e} +- {sigma_violet:.3e}")

	frequencies = [5.190, 5.494, 6.880, 7.407]
	voltage_avg = [yellow_avg, green_avg, blue_avg, violet_avg]

	coefficients = np.polyfit(frequencies, voltage_avg, 1)
	a, b = coefficients
	threshold_freq = -b / a
	
	polynomial = np.poly1d(coefficients)

	regression_line = polynomial(frequencies)

	e = 1.602e-19
	m = 1.88e-15
	h = 2 *  m * e
	print(f"{threshold_freq}")
	print(f"Planck's constant {h}")

	Lextr = h * threshold_freq * (10 ** 14) / e
	print(f"Extraction mechanical work: {Lextr}")

	plt.figure(figsize=(8, 6))
	plt.plot(frequencies, voltage_avg, 'o', color='blue', label='U = f(v)', markersize=8)
	plt.plot(frequencies, regression_line, '-', color='red', label=f'Linear regression\nU = {coefficients[0]:.3f}ν + {coefficients[1]:.3f}')
	plt.xlabel("Frequency (ν) [10^14 Hz]", fontsize=12)
	plt.ylabel("Average Voltage (U) [V]", fontsize=12)
	plt.title("U = f(ν)", fontsize=14)
	plt.grid(True)
	plt.legend()
	plt.show()
