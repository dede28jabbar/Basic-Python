import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddr = "muhammad.abdul81@ui.ac.id"
toaddr = "dede28jabbar@gmail.com"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Test Python"
password = "ini password"

body = "Hello, Selamat pagi menjelang siang!"
msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, password)
text = msg.as_string()
server.sendmail(fromaddr,toaddr, text)
server.quit()
print("Successfully sent email to %s:" % toaddr)
