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

    # def __init__(self, _user, _password, _smtpSever, _toAddress):

    @classmethod
    def send_Message_WithAttach(self, _ambiente, _toAddress, _subject, _text, _file_abspath=""):

        try:

            usuario = _ambiente.account_email
            contrasena = _ambiente.password_email
            smtpServer = _ambiente.smtp_sever
            toAddress = _toAddress

            fromAddress = usuario

            msg = MIMEMultipart(
                From=fromAddress,
                To=toAddress,
                Date=formatdate(localtime=True),
                Subject=_subject
            )

            msg.attach(MIMEText(_text))
            msg['Subject'] = _subject
            msg['From'] = fromAddress
            msg['To'] = toAddress

            if _file_abspath != "":
                msg.attach(MIMEApplication(
                    open(_file_abspath, "rb").read(),
                    Content_Disposition='attachment; filename="{0}"'.format(
                        basename(_file_abspath)),
                    Name=basename(_file_abspath)
                ))

            server = SMTP(smtpServer)
            server.login(usuario, contrasena)
            dirs = toAddress.replace(',', ' ')
            destinatario = dirs.split()
            server.sendmail(fromAddress, destinatario, msg.as_string())
            server.quit()
            return "Mensaje Enviado.......OK"

        except Exception, error:
            raise ErrorEjecucion(
                "Postman.send_Message_WithAttach()",
                type(error).__name__,
                str(error)
            )

    @classmethod
    def send_GmailMessage_WithAttach(self, _ambiente, _toAddress, _subject, _text, _file_abspath=""):

        try:

            usuario = _ambiente.account_email
            contrasena = _ambiente.password_email
            smtpServer = _ambiente.smtp_sever
            toAddress = _toAddress

            fromAddress = usuario

            msg = MIMEMultipart(
                From=fromAddress,
                To=toAddress,
                Date=formatdate(localtime=True),
                Subject=_subject
            )

            msg.attach(MIMEText(_text))
            msg['Subject'] = _subject
            msg['From'] = fromAddress
            msg['To'] = toAddress

            if _file_abspath != "":
                msg.attach(MIMEApplication(
                    open(_file_abspath, "rb").read(),
                    Content_Disposition='attachment; filename="{0}"'.format(
                        basename(_file_abspath)),
                    Name=basename(_file_abspath)
                ))

            server = SMTP(smtpServer)
            server.ehlo()
            server.starttls()
            server.login(usuario, contrasena)
            dirs = toAddress.replace(',', ' ')
            destinatario = dirs.split()
            server.sendmail(fromAddress, destinatario, msg.as_string())
            server.quit()
            return "Mensaje Enviado.......OK"

        except Exception, error:
            raise ErrorEjecucion(
                "Postman.send_Message_WithAttach()",
                type(error).__name__,
                str(error)
            )

    def get_MIME(self, _file_abspath):
        return 
# Cuenta de correo para notificaciones:
# Cuenta: notificaciones@nuvoil.com
# Contraseña: p272liq
