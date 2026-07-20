# ESP32 2D/3D Space Mapping using VL53L5CX Time-of-Flight Sensor

A real-time embedded space mapping system built using the **ESP32 DevKit V1** and the **VL53L5CX Time-of-Flight (ToF) sensor**. The project captures depth data from the sensor, transmits it over serial communication, and visualizes the environment as **2D occupancy maps**, **3D point clouds**, and **3D depth surfaces** using Python.

---

## Features

- Real-time depth acquisition using the VL53L5CX ToF sensor
- ESP32-based embedded firmware
- Serial communication between ESP32 and Python
- 2D occupancy mapping
- Interactive 3D point cloud visualization
- 3D depth surface visualization
- Accumulated environment mapping
- Modular Python visualization scripts

---

## Hardware

- ESP32 DevKit V1
- VL53L5CX 8×8 Time-of-Flight Sensor
- USB Cable

---

## Software Stack

### Embedded
- Arduino IDE
- C++

### Desktop
- Python 3
- NumPy
- Matplotlib
- PySerial

---

## Repository Structure

```text
ESP32-Space-Mapping
│
├── Arduino/
│   └── Arduino_IDE_code.ino
│
├── Python/
│   ├── 2D plot.py
│   ├── 3D PointCloud.py
│   ├── 3D DepthSurface.py
│   └── 3D DepthSurface AccumulatedMap.py
│
├── Assets/
│   ├── 2d_mapping.mp4
│   ├── point_cloud.mp4
│   ├── depth_surface.mp4
│   └── accumulated_map.mp4
│
└── README.md
```

---

## System Workflow

```text
VL53L5CX ToF Sensor
        │
        ▼
      ESP32
        │
Serial Communication
        │
        ▼
Python Visualization
        │
 ├── 2D Occupancy Map
 ├── 3D Point Cloud
 ├── 3D Depth Surface
 └── Accumulated Mapping
```

---

## Demonstrations

- 🎥 [2D Occupancy Mapping](Assets/2d_mapping.mp4)
- 🎥 [3D Point Cloud Visualization](Assets/point_cloud.mp4)
- 🎥 [3D Depth Surface Visualization](Assets/depth_surface.mp4)
- 🎥 [Accumulated 3D Environment Mapping](Assets/accumulated_map.mp4)

---

## Applications

- Indoor environment mapping
- Obstacle detection
- Robotics
- Autonomous navigation
- SLAM research
- 3D environment visualization

---

## Future Improvements

- Wireless streaming over Wi-Fi
- ROS2 integration
- Higher-resolution ToF sensors
- Sensor fusion with IMU
- Mesh reconstruction
- Real-time SLAM

---

## Author

**Nisarg Adhvaryu**

B.Tech Electronics & Communication Engineering  
Pandit Deendayal Energy University (PDEU)
