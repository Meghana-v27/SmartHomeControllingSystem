# 🏠 Smart Home Management System

## 📌 Project Overview

**Smart Home Management System** is a Python console application that lets users manage a set of smart devices in a home — lights, fans, plugs, and locks — from a single menu-driven interface.

Users can add devices, remove them, control them individually, view devices by room, turn everything on/off at once, and check device counts.

The project is developed using **Python and Object-Oriented Programming (OOP)** concepts.

It demonstrates the **four pillars of OOP**:

* 🔹 Encapsulation
* 🔹 Inheritance
* 🔹 Polymorphism
* 🔹 Abstraction

---

## 🎯 Objectives

The main objectives of this project are:

* To create and manage different types of smart devices.
* To turn devices ON/OFF and adjust their settings (brightness, speed, load).
* To lock/unlock smart locks.
* To organize and view devices by room.
* To control all devices at once (turn everything ON or OFF).
* To understand Object-Oriented Programming concepts using a real-world example.
* To practice Python classes, objects, inheritance, and abstraction.

---

## ⚙️ Features

### 💡 Add Device

Users can add a new device by choosing its type (Light, Fan, Plug, or Lock) and giving it a device ID and room name.

### ❌ Remove Device

Users can remove a device from the system using its device ID.

### 📋 View All Devices

The system displays the status of every device currently added.

### 🎛️ Control Device

Users can select a device by ID and:

* Toggle its power ON/OFF
* Set brightness (Light)
* Set speed (Fan)
* Set load in watts (Plug)
* Lock/Unlock (Lock)

### 🚪 View Room Devices

Users can view all devices that belong to a specific room.

### 🔛 Turn ON / OFF All Devices

Users can turn every controllable device ON or OFF in one action. Locks are skipped, since they aren't "powered" devices.

### 🔢 Device Count

The system displays the total number of devices currently added.

---

## 🛠️ Technologies Used

* **Python**
* **Object-Oriented Programming**
* **Classes and Objects**
* **Abstract Base Classes (`abc` module)**
* **Inheritance**
* **Polymorphism**
* **Encapsulation**
* **Abstraction**

---

# 🧩 OOP Concepts Used

## 1. 🔒 Encapsulation

Encapsulation means keeping the data and methods together inside a class and controlling how the data is accessed. `_device_id` is stored as a "private" attribute and only exposed through a read-only `property`.

```python
class SmartDevice(ABC):
    def __init__(self, device_id, room):
        self._device_id = device_id
        self.room = room
        self.is_on = False

    @property
    def device_id(self):
        return self._device_id
```

The internal state (`_brightness`, `_speed`, `_power_watts`) is also kept private inside each subclass and only changed through validated methods like `set_brightness()` or `set_speed()`.

---

## 2. 👨‍👩‍👧 Inheritance

`SmartLight`, `SmartFan`, `SmartPlug`, and `SmartLock` all inherit shared behavior (device ID, room, power state, percentage validation) from the base `SmartDevice` class.

```python
class SmartDevice(ABC):
    def __init__(self, device_id, room):
        self._device_id = device_id
        self.room = room
        self.is_on = False

class SmartFan(SmartDevice):
    def __init__(self, device_id, room):
        super().__init__(device_id, room)
        self._speed = 0
        self.device_type = 'Fan'
```

`SmartFan` reuses `device_id`, `room`, `is_on`, and `_validate_percentage()` from `SmartDevice` instead of rewriting them.

---

## 3. 🔄 Polymorphism

Every device type implements `get_status()` and `toggle_power()` differently, but the `SmartHome` class calls them the same way for every device — it doesn't need to know which subclass it's dealing with.

```python
class SmartLight(SmartDevice):
    def get_status(self):
        state = 'ON' if self.is_on else 'OFF'
        print(f'Device: Light | ... | Power: {state:<3} | (Brightness: {self._brightness}%)')

class SmartLock(SmartDevice):
    def get_status(self):
        state = 'LOCKED' if self.is_locked else 'UNLOCKED'
        print(f'Device: Lock  | ... | Status: {state}')
```

In `SmartHome.show_all_devices()`, the same line `device.get_status()` produces different output depending on the actual device type.

---

## 4. 🎭 Abstraction

`SmartDevice` is an **abstract base class** (using Python's `ABC`). It defines *what* every device must do (`toggle_power()`, `get_status()`) without saying *how* — each subclass fills in the details. This also means `SmartDevice` itself can never be instantiated directly.

```python
class SmartDevice(ABC):
    @abstractmethod
    def toggle_power(self):
        pass

    @abstractmethod
    def get_status(self):
        pass
```

A user of `SmartHome` only needs to call `home.toggle_device(device_id)` — they don't need to know how each device type turns itself on or off internally.

---

# 🏗️ Project Structure

```text
Smart-Home-Management-System/
│
├── smarthome.py
├── README.md
└── requirements.txt
```

### `smarthome.py`

Contains the `SmartDevice` abstract class, all device subclasses (`SmartLight`, `SmartFan`, `SmartPlug`, `SmartLock`), the `SmartHome` manager class, and the menu-driven `main()` program.

### `README.md`

Contains information about the project, features, OOP concepts, and usage.

### `requirements.txt`

Contains the required Python packages. Since this project only uses Python's standard library (`abc`), no external packages are required.

---

# ▶️ How to Run the Project

### Step 1: Install Python

Make sure Python is installed on your computer.

```bash
python --version
```

### Step 2: Clone the Repository

```bash
git clone <your-github-repository-link>
```

### Step 3: Open the Project

```bash
cd Smart-Home-Management-System
```

### Step 4: Run the Program

```bash
python smarthome.py
```

---

# 💻 Example

```text
==========================
SMART HOME MANAGEMENT SYSTEM
============================
1.Add Device
2.Remove Device
3.View all Devices
4.Control Device
5.View Room Devices
6.Turn ON ALL Devices
7.Turn OFF ALL Devices
8.Count Devices
9.Exit
====================================
Enter your choice: 3

======== ALL DEVICES =======
Device: Light | [Zone] : Zone-A  | Room: Live Room | Power: OFF | (Brightness: 0%)
Device: Light | [Zone] : Zone-M  | Room: Bed Room  | Power: OFF | (Brightness: 0%)
Device: Fan   | [Zone] : Fan-01  | Room: Bed Room  | Power: OFF | (Speed: 0%)
Device: Plug  | [Zone] : Plug-01 | Room: Balcony   | Power: OFF | (Load: 0W)
Device: Plug  | [Zone] : Plug-02 | Room: Kitchen   | Power: OFF | (Load: 0W)
Device: Lock  | [Zone] : Lock-01 | Room: Front Door | Status: LOCKED
======================
```

---

# 🌱 Supported Device Types

The system currently supports:

* 💡 Smart Light — adjustable brightness (0–100%)
* 🌀 Smart Fan — adjustable speed (0–100%)
* 🔌 Smart Plug — adjustable load in watts
* 🔒 Smart Lock — lock/unlock control

New device types can be added by creating another subclass of `SmartDevice`.

---

# 📚 Concepts Learned

Through this project, the following Python concepts can be practiced:

* Variables
* Input and Output
* Conditional Statements
* Loops
* Functions
* Classes and Objects
* Constructors (`__init__`)
* Properties (`@property`)
* Methods
* Encapsulation
* Inheritance
* Polymorphism
* Abstraction (`ABC`, `@abstractmethod`)
* Basic Input Validation

---

# 🚀 Future Enhancements

The project can be improved by adding:

* 🗄️ Database or file-based persistence (so devices aren't lost on exit)
* 🖥️ Graphical User Interface (GUI)
* 🌐 Web application version
* 📱 Mobile application
* ⏰ Scheduling (auto ON/OFF at set times)
* 🔔 Notifications/alerts
* 🔐 User authentication
* 📊 Energy usage tracking and reports

---

# 👨‍💻 Author

**Your Name Here**

B.Tech – Computer Science and Engineering

---

# ⭐ Conclusion

The **Smart Home Management System** is a Python-based console application that demonstrates how **Object-Oriented Programming** — encapsulation, inheritance, polymorphism, and abstraction — can be used to model and control a real-world system of smart devices.
