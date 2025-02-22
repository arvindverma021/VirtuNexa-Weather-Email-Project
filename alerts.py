import smtplib
from email.mime.text import MIMEText
from config import EMAIL_SENDER, EMAIL_PASSWORD  # Import sender credentials

def send_alert(recipient_email, city, temperature, condition):
    try:
        msg = MIMEText(f"Alert! The temperature in {city} is {temperature}°C with {condition}.")
        msg["Subject"] = f'Weather Alert for {city}'
        msg["From"] = EMAIL_SENDER
        msg["To"] = 'aviverma021@gmail.com'  #  Receiver's email

        # Connect to SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, recipient_email, msg.as_string())  # 👈 Send email
        server.quit()

        print(f"✅ Email sent successfully to {recipient_email}!")
    except Exception as e:
        print(f"❌ Error sending email: {e}")
