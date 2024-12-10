# Python Keylogger Project

This is a Python-based keylogger that logs keystrokes, takes periodic screenshots, and sends them to a specified email address. The project runs in the background, logs the keys typed, takes screenshots, and emails the captured data at regular intervals.

## Features

- **Keystroke Logging**: Captures all keys typed on the computer.
- **Screenshot Capturing**: Takes screenshots at specified intervals.
- **Email Sending**: Sends captured logs and screenshots to a specified email address.
- **Cross-Platform**: Works on Windows and Linux systems.
- **No Remote Server**: The data is stored locally and emailed to the user.
- **Keylogger Stops on ESC**: The keylogger can be stopped by pressing the ESC key.

## 📧 Example of Email Logs

**Subject**: Keylogger Logs  
**Body**:

#...json
#...{   
#...  "Notepad": "This is a test log" 
#...}

# Attachments: Screenshots from the screenshots/ folder.

 File Structure
plaintext
Copy code
Python-Keylogger/
│
├── keylogger.py                # Main keylogger script
├── .gitignore                  # Git ignore file
├── .env                        # Environment variables file
├── requirements.txt            # Dependencies for the project
├── key_log.json                # Captured key logs
├── screenshots/                # Directory for screenshots
└── src/                        # Source code folder
🛠 Installation
Step 1: Clone the Repository
bash
Copy code
git clone https://github.com/ArvinSuvarna/Python-Keylogger.git
Step 2: Install Dependencies
Make sure you have Python 3.x installed, then install the required libraries.

bash
Copy code
pip install -r requirements.txt
Step 3: Set Up Environment Variables
Create a .env file in the project directory with the following content:

plaintext
Copy code
EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=your_email_password
EMAIL_RECEIVER=receiver_email@gmail.com
Step 4: Run the Keylogger
To run the keylogger, simply execute:

bash
Copy code
python keylogger.py
The keylogger will start running, logging the keystrokes and taking screenshots as specified.

🖥 Compilation to EXE
If you'd like to compile the script into an executable for Windows, you can use PyInstaller.

Install PyInstaller:

bash
Copy code
pip install pyinstaller
Compile the keylogger script:

bash
Copy code
pyinstaller --onefile --noconsole keylogger.py
This will generate an executable (keylogger.exe) that can be run directly without needing Python installed.

❓ How It Works
Keylogger: Uses pynput to listen for keystrokes and logs them.
Screenshots: Takes periodic screenshots using Pillow.
Email Sending: Uses the smtplib library to send emails with logs and screenshots as attachments.
File Logging: Saves captured keystrokes and screenshots locally.
⚠️ Important Disclaimer
This keylogger is for educational purposes only. Use it responsibly and ethically. Do not deploy this script without proper consent and authorization. Unauthorized use of keyloggers is illegal and unethical.

🧑‍💻 Contributing
Feel free to fork this repository and contribute by submitting pull requests. Please follow the coding standards and guidelines when contributing.

📜 License
This project is open-source and licensed under the MIT License.
