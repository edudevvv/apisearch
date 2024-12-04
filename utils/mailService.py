from smtplib import SMTP, SMTPException
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class mailService:
    def __init__(self, domain: str):
        self.server = SMTP(f"smtp.{domain}", 587)

    def connect(self, user: str, password: str):
      try:
          self.user = user

          self.server.starttls()
          self.server.login(user, password)

          return True
      except Exception as e:
          return False
      
    def sendMail(self, clientName: str, clientMail: str, subject: str, body: str):
        try: 
            messageService = MIMEMultipart()
            messageService["From"] = f"{clientName} <{self.user}>"
            messageService["To"] = clientMail
            messageService["Subject"] = subject

            messageService.attach(MIMEText(body, "html"))
            mailInfo = self.server.sendmail(self.user, clientMail, messageService.as_string())
            
            if mailInfo == {}:
                return True
        except SMTPException as exceptionMail: 
            return False
        except Exception as exception:
            return False
        