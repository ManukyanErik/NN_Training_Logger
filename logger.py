import smtplib
import ssl
from email.message import EmailMessage


class Logger:
    def __init__(self, min_log_level='DEBUG', email_sender=None,  email_password=None):
        self.min_log_level = min_log_level
        self.sender = Sender(email_sender, email_password)
        self.consoleLog = ConsoleLog()
        self.receivers_emails = {"DEBUG": [], "INFO": [], "WARNING": [], "ERROR": []}

    def add_email_receiver(self, mail, *lvls):
        for lvl in lvls:
            self.receivers_emails[lvl].append(mail)

    def log(self, message, log_level="INFO"):
        if self._is_valid_log_level(log_level) and self._is_log_level_enabled(log_level):
            for mail in self.receivers_emails[log_level]:
                self.sender.send_email(mail, message)
            self.consoleLog.print_log(message, log_level)

    def _is_valid_log_level(self, log_level):
        valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR"]
        if log_level not in valid_levels:
            print(f"Invalid log level: {log_level}")
            return False
        return True

    def _is_log_level_enabled(self, log_level):
        log_levels = ["DEBUG", "INFO", "WARNING", "ERROR"]
        return log_levels.index(log_level) >= log_levels.index(self.min_log_level)
    

class Sender:
    def __init__(self, mail_sender, email_password):
        self.mail_sender = mail_sender
        self.email_password = email_password

    def send_email(self, email_receiver ,message):
        email_sender = self.mail_sender
        # Enable 2-step verification and provide the generated password instead of the account password in the code.
        # https://www.youtube.com/watch?v=g_j6ILT-X0k&t=136s
        email_password = self.email_password
        # Set the subject and body of the email
        subject = 'Logger'
        body = message

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)

        # Add SSL (layer of security)
        context = ssl.create_default_context()

        # Log in and send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls(context=context)
            smtp.login(email_sender, email_password)
            smtp.send_message(em)

# #         print(f"Message -> {message} <- send to -> {email} <- email.") 
         

class ConsoleLog:
    def print_log(self, message, log_level):
        print(f"[{log_level}] {message}")

