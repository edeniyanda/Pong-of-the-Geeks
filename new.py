import numpy as np
import matplotlib.pyplot as plt

# Time array
t = np.linspace(0, 0.02, 1000)  # 0 to 20 ms

# Voltage and current waveforms
v = 400 * np.sin(100 * np.pi * t + 0.785)
i = 20 * np.sin(100 * np.pi * t + 0.524)

# Plotting the waveforms
plt.figure(figsize=(10, 6))
plt.plot(t, v, label='Voltage (v(t))')
plt.plot(t, i, label='Current (i(t))', linestyle='--')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Voltage and Current Waveforms')
plt.legend()
plt.grid(True)
plt.show()
