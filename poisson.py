import math
import matplotlib.pyplot as plt

def main():
	a = 2.8
	N = 1028
	P = []
	kth = []
	res = []
	kexp = [62, 174, 247, 232, 147, 97, 41, 21, 5, 0, 2]
	sum_res = 0
	fact = 1

	for x in range(0, 11):
		c = (math.e ** (-a)) * (a ** x) / (fact)
		fact *= (x + 1)
		d = N * P[x]
		P.append(c)
		kth.append(d)
		tmp = ((kth[x] - kexp[x]) ** 2) / kth[x]
		print(f"{c:.3e}, {d}, {tmp}")
		sum_res += tmp
		res.append(tmp)

	print(sum_res)
	x_values = list(range(11))
	plt.bar(x_values, kexp, width=0.4, label="Observed (kexp)", color="blue", align='center')
	plt.bar(x_values, kth, width=0.4, label="Expected (kth)", color="orange", align='edge')
	plt.xlabel("x")
	plt.ylabel("Frequency")
	plt.title("Comparison of Observed and Expected Frequencies")
	plt.legend()
	plt.show()

if __name__ == "__main__":
	exit(main())
