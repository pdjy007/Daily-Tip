import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import schedule
import time
import os
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
USERNAME = os.getenv("pdjy007@gmail.com")  
PASSWORD = os.getenv("ubmkqbeoyhycrwbd")  
TO_EMAIL = "vhemanthsai68@gmail.com"
def get_python_tip():
    tips = [
        "Tip: Use list comprehensions for concise and readable code.",
        "Tip: Use the `enumerate()` function to get both index and value when looping through a list.",
        "Tip: Use `zip()` to iterate over multiple lists in parallel.",
        "Tip: List comprehensions can include conditional logic. Example: [x for x in range(10) if x % 2 == 0]",
        "Tip: Use `defaultdict` from the `collections` module to handle missing keys in dictionaries.",
        "Tip: Use `with` to manage file operations and ensure files are properly closed.",
        "Tip: The `join()` method is a more efficient way to concatenate strings than using `+` in a loop.",
        "Tip: Use `try-except` blocks to handle exceptions and avoid crashes.",
        "Tip: `lambda` functions are small anonymous functions defined with the `lambda` keyword.",
        "Tip: Use `map()` to apply a function to all items in an iterable.",
        "Tip: Use `filter()` to filter elements of an iterable based on a function.",
        "Tip: Use `sorted()` to sort an iterable without modifying the original.",
        "Tip: `set` is a data structure that removes duplicates and supports mathematical operations like union and intersection.",
        "Tip: Use `collections.Counter` to count occurrences of elements in an iterable."
    ]
    today = datetime.now()
    day_of_year = today.timetuple().tm_yday
    index = day_of_year % len(tips)
    return tips[index]
def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = USERNAME
    msg['To'] = TO_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(USERNAME, PASSWORD)
            server.send_message(msg)
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error: {e}")
def job():
    subject = "Daily Python Tip"
    body = get_python_tip()
    send_email(subject, body)
if __name__ == "__main__":
    schedule.every().day.at("00:39").do(job)
    while True:
        schedule.run_pending()
        time.sleep(60)  