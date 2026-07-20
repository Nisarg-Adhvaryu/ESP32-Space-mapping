import serial
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import threading

# CONFIG
PORT = "COM3"   # change if needed
BAUD = 115200
GRID = 4

latest_points = []
lock = threading.Lock()

# SERIAL THREAD
def serial_reader():
    global latest_points
    ser = serial.Serial(PORT, BAUD, timeout=1)

    while True:
        line = ser.readline().decode(errors='ignore').strip()
        values = line.split(',')

        if len(values) == GRID * GRID:
            try:
                distances = np.array(values, dtype=float).reshape(GRID, GRID)

                points = []

                for i in range(GRID):
                    for j in range(GRID):
                        z = distances[i][j]

                        if z == 0:
                            continue

                        # normalize grid to [-1, 1]
                        x = (j - (GRID-1)/2)
                        y = (i - (GRID-1)/2)

                        # scale
                        points.append([x, -y, z])

                with lock:
                    latest_points = points

            except:
                pass

# PLOT
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def update():
    while True:
        ax.clear()

        with lock:
            pts = np.array(latest_points)

        if len(pts) > 0:
            ax.scatter(pts[:,0], pts[:,1], pts[:,2], c=pts[:,2], cmap='jet')

        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z (mm)")
        ax.set_title("Live 3D Point Cloud")

        ax.set_xlim(-2, 2)
        ax.set_ylim(-2, 2)
        ax.set_zlim(0, 3000)

        plt.pause(0.1)

# START
threading.Thread(target=serial_reader, daemon=True).start()
update()