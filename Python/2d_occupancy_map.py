import serial
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import threading

PORT = "COM3"
BAUD = 115200
GRID = 4

latest_frame = np.zeros((GRID, GRID))
lock = threading.Lock()

def serial_reader():
    global latest_frame
    ser = serial.Serial(PORT, BAUD, timeout=1)
    print(f"Connected to {PORT}")

    while True:
        line = ser.readline().decode(errors='ignore').strip()
        
        if not line:
            continue

        print("RAW:", line)   # 👈 DEBUG

        values = line.split(',')

        if len(values) == GRID * GRID:
            try:
                data = np.array(values, dtype=float).reshape(GRID, GRID)
                data[data == 0] = np.nan

                with lock:
                    latest_frame = data
            except:
                pass

# Plot
fig, ax = plt.subplots()
im = ax.imshow(np.zeros((GRID, GRID)), cmap='jet', vmin=0, vmax=3000)
plt.colorbar(im)

texts = [[ax.text(j, i, "", ha='center', va='center', color='white')
          for j in range(GRID)] for i in range(GRID)]

def update(frame):
    with lock:
        data = latest_frame.copy()

    im.set_data(data)

    for i in range(GRID):
        for j in range(GRID):
            val = data[i, j]
            texts[i][j].set_text("--" if np.isnan(val) else int(val))

    return [im] + [t for row in texts for t in row]

threading.Thread(target=serial_reader, daemon=True).start()
ani = animation.FuncAnimation(fig, update, interval=200)

plt.show()
