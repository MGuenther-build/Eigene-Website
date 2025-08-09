import smtplib
import ssl
import os


def mailen(message):
    host = "smtp.gmail.com"
    port = 465
    username = "Protools1802@gmail.com"
    passwort = os.getenv("PASSWORT")                                     # über Google zu 2FA App-Passwort und dort alles generieren lassen (niemals sein Hauptpasswort nehmen!)
    receiver = "Protools1802@gmail.com"                                 # dann Umgebungsvariablen in Windows Sart suchen, dort Benutzervariablen auf "neu" und dort "PASSWORT"
    mycontext = ssl.create_default_context()                            # als Name anlegen, und als Wert der Variablen wird das erzeugte Google Passwort eingegeben
    with smtplib.SMTP_SSL(host, port, context=mycontext) as server:
        server.login(username, passwort)
        server.sendmail(username, receiver, message)
