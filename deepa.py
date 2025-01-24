import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def send_email(sender_email, sender_password, recipient_email, subject, body, attachment_path=None):
    try:
        # Set up the MIME
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Add email body
        msg.attach(MIMEText(body, 'plain'))

        # Attach a file if specified
        if attachment_path and os.path.isfile(attachment_path):
            with open(attachment_path, 'rb') as attachment_file:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment_file.read())
                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename={os.path.basename(attachment_path)}'
                )
                msg.attach(part)

        # Connect to the SMTP server and send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())

        print("Email sent successfully.")

    except Exception as e:
        print(f"Failed to send email: {e}")

# Example usage
def main():
    sender_email = "thanideepa1@gmail.com"
    sender_password = "Deepa_0812"  # Use an app password for Gmail
    recipient_email = "jananiramesh183@gmail.com"
    subject = "Test Email with Attachment"
    body = "This is a test email with an optional attachment."
    attachment_path = r'C:\Users\Deepa\Documents\test.txt'  # Use raw string for Windows path

    send_email(sender_email, sender_password, recipient_email, subject, body, attachment_path)

if __name__ == "__main__":
    main()
