import matplotlib.pyplot as plt

E_centrul = [662, 128, 1226.3, 1156, 1408, 661.7, 1332.5]
n_centru = [1200, 2471, 2567, 2400, 1340, 1256, 2566]
plt.figure(figsize=(8, 6))
plt.plot(E_centrul, n_centru, marker='o', linestyle='-', color='b', label='n_centrul vs. E_centrul')
plt.xlabel('E_centrul (keV)', fontsize=12)
plt.ylabel('n_centrul (maximum)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)
plt.show()