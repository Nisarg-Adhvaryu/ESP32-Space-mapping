import serial
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
import threading

PORT = "COM3"
BAUD = 115200
GRID = 4

# ================= SHARED =================
latest_frame = np.zeros((GRID, GRID))
lock = threading.Lock()

# ================= SERIAL THREAD =================
def serial_reader():
    global latest_frame
    ser = serial.Serial(PORT, BAUD, timeout=1)

    while True:
        line = ser.readline().decode(errors='ignore').strip()

        if "," not in line:
            continue

        values = line.split(',')
        if len(values) != GRID * GRID:
            continue

        try:
            frame = np.array(values, dtype=float).reshape(GRID, GRID)

            with lock:
                latest_frame = frame
        except:
            pass

threading.Thread(target=serial_reader, daemon=True).start()

# ================= PLOT =================
plt.ion()
fig = plt.figure(figsize=(10,5))

ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')

prev = np.zeros((GRID, GRID))
alpha = 0.7
accumulated = []

x = np.arange(GRID)
y = np.arange(GRID)
X, Y = np.meshgrid(x, y)

while True:
    with lock:
        frame = latest_frame.copy()

    # 🔥 smoothing
    prev = alpha * prev + (1 - alpha) * frame
    Z = gaussian_filter(prev, sigma=1)

    # ================= SURFACE =================
    ax1.cla()
    ax1.plot_surface(X, Y, Z, cmap='viridis')
    ax1.set_title("3D Depth Surface")
    ax1.set_zlim(0, 2500)

    # ================= ACCUMULATION =================
    for i in range(GRID):
        for j in range(GRID):
            z = Z[i][j]
            if z <= 0:
                continue
            accumulated.append([j-1.5, i-1.5, z])

    if len(accumulated) > 2000:
        accumulated = accumulated[-2000:]

    pts = np.array(accumulated)

    ax2.cla()
    if len(pts) > 0:
        ax2.scatter(pts[:,0], pts[:,1], pts[:,2],
                    c=pts[:,2], cmap='jet', s=5)

    ax2.set_title("Accumulated Map")
    ax2.set_zlim(0, 2500)

    plt.pause(0.05)
