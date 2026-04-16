# 📊 Automated Platform Surveillance System

## 📌 Overview

The **Automated Platform Surveillance System** is a powerful Python-based monitoring tool designed to track system performance in real time. It continuously monitors CPU, RAM, Disk usage, and running processes, while automatically generating structured log files at defined intervals for analysis, debugging, and system optimization.

---

## 🚀 Key Features

✨ Real-time CPU usage monitoring
✨ Detailed RAM (Memory) tracking
✨ Disk space analysis
✨ Process monitoring with memory consumption
✨ Automatic timestamp-based log generation
✨ Smart scheduling using interval-based execution
✨ Lightweight and command-line driven

---

## 🛠️ Technologies Used

* **Python** 🐍
* **psutil** → System resource monitoring
* **schedule** → Task automation
* **os, sys, time** → Core Python modules

---

## 📂 Project Structure

```
Automated-Platform-Surveillance-System/
│
├── surveillance.py
├── Logs/
└── README.md
```

---

## ⚙️ Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### Step 2: Install Required Libraries

```bash
pip install psutil schedule
```

---

## ▶️ Usage

### 🔹 Help Command

```bash
python surveillance.py --h
```

### 🔹 Usage Instructions

```bash
python surveillance.py --u
```

### 🔹 Run the Script

```bash
python surveillance.py <TimeInterval> <DirectoryName>
```

### ✅ Example

```bash
python surveillance.py 5 Logs
```

📌 This will generate a new log file every **5 minutes** inside the `Logs` folder.

---

## 📝 Log File Details

Each generated log file includes:

* 🕒 Timestamp of creation
* ⚙️ CPU Usage (%)
* 🧠 RAM Details (Total, Used, Available)
* 💾 Disk Usage Statistics
* 📋 Running Processes

  * PID
  * Process Name
  * Memory Usage

---

## ⚠️ Error Handling

✔️ Handles invalid command-line arguments
✔️ Skips inaccessible or restricted processes
✔️ Validates and creates directories safely

---

## 📈 Future Enhancements

🚀 Email alerts for high resource usage
🚀 Web-based dashboard for real-time monitoring
🚀 Graphical visualization of logs
🚀 Database integration instead of file storage

---

## 👨‍💻 Author

**Saurabh Bhonsle**

---

## 📜 License

This project is open-source and free to use for **educational and learning purposes**.

---

💡 *Built with the vision to understand system internals and create real-world monitoring tools.*

