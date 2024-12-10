# Python Keylogger with Advanced Features 🔑📸

<p align="center"> <img src="https://via.placeholder.com/700x250.png?text=Python+Keylogger+Project" alt="Keylogger Banner"> </p>

## 📖 Overview
This project is a Python-based keylogger designed for **educational and ethical purposes only**. It demonstrates how keylogging works while integrating additional features like screenshot capturing and email-based reporting. The project also allows users to compile the keylogger as a standalone executable.

> ⚠️ **Disclaimer**: This tool is strictly for educational purposes. The author is not responsible for any misuse of the tool. Always respect privacy and ensure ethical usage.

---

## 🚀 Features

- **Keystroke Logging**: Captures all keystrokes and logs them into a JSON file categorized by active applications.
- **Screenshot Capturing**: Periodically captures screenshots and stores them locally.
- **Email Reporting**: Sends both key logs and screenshots to a specified email at regular intervals.
- **Standalone Executable**: Runs as a compiled `.exe` file for ease of use and background operation.
- **No Remote Server**: Unlike other implementations, this keylogger does not rely on a remote server, ensuring local storage and minimal dependencies.

---

## 🖥️ Screenshots of Features

### **Sample Key Logs**

```json
{   
  "Notepad": "This is a test log" 
}

Captured Screenshots
<img src="https://via.placeholder.com/600x300" alt="Screenshot Example" width="600">
📂 File Structure
bash
Copy code
Python-Keylogger/
│
├── keylogger.py         # Main Python script
├── requirements.txt     # Python dependencies
├── .env                 # Email credentials (excluded in repo)
├── screenshots/         # Folder to store captured screenshots
├── LICENSE              # License file
└── README.md            # Project documentation
📦 Installation Guide
Option 1: Running the Python Script
Clone the Repository
Open a terminal and run:

bash
Copy code
git clone https://github.com/your-username/Python-Keylogger.git
cd Python-Keylogger
Set up a Virtual Environment

bash
Copy code
python -m venv .venv
source .venv/bin/activate  # For Windows: .venv\Scripts\activate
Install Dependencies

bash
Copy code
pip install -r requirements.txt
Configure Environment Variables

Create a .env file in the root directory:
plaintext
Copy code
EMAIL_SENDER=your-email@gmail.com
EMAIL_PASSWORD=your-password
EMAIL_RECEIVER=receiver-email@gmail.com
Replace placeholders with your actual credentials.
Run the Keylogger

bash
Copy code
python keylogger.py
Option 2: Running the Compiled Executable
Compile the Python script into an executable file using pyinstaller:

bash
Copy code
pyinstaller --onefile --noconsole keylogger.py
The executable will be located in the dist/ folder.
Test the .exe File

Run the executable file by double-clicking it.
It will log keystrokes and capture screenshots as per your settings.
✨ Usage Instructions
Keylogger Output

Keystrokes are logged in key_log.json, categorized by application.
Screenshots are saved in the screenshots/ folder.
Email Reporting

Emails are sent at regular intervals (default: 5 minutes) to the specified email.
Logs and screenshots are attached to the email.
Stopping the Keylogger

Press the ESC key in any application to stop the keylogger.
📜 Installation of the Keylogger via USB (Optional)
Copy the compiled .exe file onto a USB drive.
On the target system, run the .exe to activate the keylogger.
The keylogger will run silently in the background.
Note: Auto-run from USB is restricted in modern systems due to security protocols. This method requires manual execution.

🔒 How to Prevent Keylogging Attacks
Do not download unknown or untrusted files from the internet.
Enable antivirus software and ensure it is up to date.
Avoid connecting untrusted USB devices to your system.
Use anti-keylogger tools to detect suspicious activity.
📧 Example of Email Logs
Subject: Keylogger Logs
Body:

json
Copy code
{   
  "Notepad": "This is a test log" 
}
Attachments: Screenshots from the screenshots/ folder.

⚙️ Customization Options
Adjust Logging and Screenshot Intervals
Modify the following constants in keylogger.py:

python
Copy code
EMAIL_INTERVAL = 300  # Time in seconds (default: 5 minutes)
SCREENSHOT_INTERVAL = 60  # Time in seconds (default: 1 minute)
Change Email Credentials
Update the .env file with new credentials as needed.

Disable Email Reporting
Comment out or remove the send_email() function in the script.

📋 Disclaimer
This tool is strictly for educational purposes. Using this tool to monitor individuals without their knowledge or consent is illegal and unethical. Always ensure you have appropriate permissions before using it.

🎓 How to Contribute
Fork the repository.
Create a new branch: git checkout -b feature-name.
Commit your changes: git commit -m "Add feature".
Push the branch: git push origin feature-name.
Submit a pull request.
📜 License
This project is licensed under the MIT License.

🌟 Show Your Support
If you found this project useful, please consider ⭐ starring the repository!

<p align="center"> <b>Made with ❤️ by Your Name</b> </p> ```
