Here's a Python program that sends automated emails with attachments using the smtplib and email libraries. This script includes customizable sender and recipient details, subject, body text, and support for file attachments.

features:

1. SMTP Configuration: The script uses Gmail's SMTP server (smtp.gmail.com), but you can replace it with your provider's SMTP settings.

2. File Attachments: Attach a file by specifying its path. If no file is provided or the path is invalid, it skips the attachment step.

3. Secure Connection: Establishes a secure connection using starttls.

Prerequisites:

1. SMTP Access: Ensure SMTP access is enabled for the sender's email account. For Gmail, you may need to use an app-specific password or enable "Less secure app access.

2. Install Libraries: No additional libraries are required; both smtplib and email are built-

Feel free to modify the script for your specific needs.
