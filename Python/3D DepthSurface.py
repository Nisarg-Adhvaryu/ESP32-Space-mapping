import serial
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

PORT = "COM3"
BAUD = 115200
GRID = 4

ser = serial.Serial(PORT, BAUD, timeout=1)

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 🔥 smoothing memory
prev = np.zeros((GRID, GRID))

alpha = 0.7  # smoothing factor

while True:
    line = ser.readline().decode(errors='ignore').strip()

    if "," not in line:
        continue

    values = line.split(',')
    if len(values) != GRID * GRID:
        continue

    try:
        Z = np.array(values, dtype=float).reshape(GRID, GRID)

        # 🔥 exponential smoothing (removes jitter)
        prev = alpha * prev + (1 - alpha) * Z

        # 🔥 spatial smoothing
        Z_smooth = gaussian_filter(prev, sigma=1)

        x = np.arange(GRID)
        y = np.arange(GRID)
        X, Y = np.meshgrid(x, y)

        ax.clear()

        # 🔥 3D surface
        ax.plot_surface(X, Y, Z_smooth, cmap='jet')

        ax.set_zlim(0, 2500)
        ax.set_title("3D Depth Surface")

        plt.pause(0.1)

    except:
        pass