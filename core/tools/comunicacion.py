# -*- coding: utf-8 -*-

# Liberias Python
from smtplib import SMTP
from os.path import basename
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate

# Librerias propias
from mistakes import ErrorEjecucion


class Postman(object):

    def __init__(self, _fromEmailAccount, _password, _smtpSever):

        self.fromAddress = _fromEmailAccount
        self.contrasena = _password
        self.smtpServer = _smtpSever

    def send_Message_WithAttach(self, _toAddress, _subject, _text, _file_abspath=""):

        try:

            msg = MIMEMultipart(
                From=self.fromAddress,
                To=_toAddress,
                Date=formatdate(localtime=True),
                Subject=_subject
            )

            msg.attach(MIMEText(_text))
            msg['Subject'] = _subject
            msg['From'] = self.fromAddress
            msg['To'] = _toAddress

            if _file_abspath != "":
                msg.attach(MIMEApplication(
                    open(_file_abspath, "rb").read(),
                    Content_Disposition='attachment; filename="{0}"'.format(
                        basename(_file_abspath)),
                    Name=basename(_file_abspath)
                ))

            server = SMTP(self.smtpServer)
            server.login(self.fromAddress, self.contrasena)
            dirs = _toAddress.replace(',', ' ')
            destinatario = dirs.split()
            server.sendmail(self.fromAddress, destinatario, msg.as_string())
            server.quit()

            print "Mensaje Enviado.......OK"

        except Exception, error:
            raise ErrorEjecucion(
                "Postman.send_Message_WithAttach()",
                type(error).__name__,
                str(error)
            )

    def send_GmailMessage_WithAttach(self, _toAddress, _subject, _text, _file_abspath=""):

        try:

            msg = MIMEMultipart(
                From=self.fromAddress,
                To=_toAddress,
                Date=formatdate(localtime=True),
                Subject=_subject
            )

            msg.attach(MIMEText(_text))
            msg['Subject'] = _subject
            msg['From'] = self.fromAddress
            msg['To'] = _toAddress

            if _file_abspath != "":
                msg.attach(MIMEApplication(
                    open(_file_abspath, "rb").read(),
                    Content_Disposition='attachment; filename="{0}"'.format(
                        basename(_file_abspath)),
                    Name=basename(_file_abspath)
                ))

            server = SMTP(self.smtpServer)
            server.ehlo()
            server.starttls()
            server.login(self.fromAddress, self.contrasena)
            dirs = _toAddress.replace(',', ' ')
            destinatario = dirs.split()
            server.sendmail(self.fromAddress, destinatario, msg.as_string())
            server.quit()

            print "Mensaje Enviado.......OK"

        except Exception, error:
            raise ErrorEjecucion(
                "Postman.send_Message_WithAttach()",
                type(error).__name__,
                str(error)
            )


# Cuenta de correo para notificaciones:
# Cuenta: notificaciones@nuvoil.com
# Contraseña: p272liq
