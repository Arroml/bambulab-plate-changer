# 🖨️ BambuLab Print Manager with Auto Plate Changer

📌 Project Overview

This project aims to integrate a Bambu Lab 3D printer with an automatic build plate changer.

The goal:
	•	A Docker container runs on a Raspberry Pi (or any host).
	•	It monitors the printer and detects when a print job has finished.
	•	Once completed, the plate changer swaps in a fresh build plate.
	•	New print jobs can be uploaded via a simple web interface (drag & drop STL/GCode files) and automatically queued.

This allows for multiple prints to run sequentially without manual intervention.

👉 Hardware: Auto Build Plate Changer for A1 Mini (Makerworld)

⸻

🚀 Features (planned & implemented)
	•	Python web server (Flask or FastAPI) for file upload & queue management
	•	Printer communication (detect job finished)
	•	Plate changer control (GPIO / serial / USB – depending on hardware)
	•	Job queue system: execute prints in sequence
	•	Dockerized for easy deployment on Raspberry Pi / NAS
	•	Logging & notifications (optional: Telegram, Discord, or Home Assistant integration)

⸻

🛠️ Installation & Setup

1. Clone the repo
