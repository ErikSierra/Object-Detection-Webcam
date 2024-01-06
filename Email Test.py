import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

USER = "erik.sierra77@gmail.com"  # Your Gmail address
PASS = "xqyd ijkw liwm hcvk"  # Your app password

# Create the container (outer) email message
msg = MIMEMultipart()
msg['Subject'] = 'Test Email Subject'  # The subject of your email
msg['From'] = USER
msg['To'] = USER
body = 'TEST 123'  # The body of your email
msg.attach(MIMEText(body, 'plain'))

# Connect to the Gmail SMTP server and send the email
s = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # Use Gmail's SMTP server address
s.login(USER, PASS)
s.sendmail(USER, USER, msg.as_string())  # Send the email
s.quit()
print("Email sent successfully")