"""
Importamos la librería estándar de Python Simple Mail Transfer Protocol (SMTP)
Nos pérmite conectarnos a servidores de correo (como Gmail) y enviar emails desde código
"""
import smtplib
"""
Importamos la clase EmailMessage del paquete estándar de Python (email.message)
Esta clase nos ayuda a crear y estructurar un email completo 
"""
from email.message import EmailMessage

# Datos
me = "zap1261@amerike.edu.mx"
you = "zap1261@amerike.edu.mx"

"""
Desde 2022 gmail bloquea la autentificación con la contraseña real
por lo que usamos las contraseñas de aplicación de gmail, estos nos permite enviar los mails de manera segura
"""
app_password = "a" 

# Pedimos datos del usuario que va enviar el correo para imprimirlos en el mensaje enviado
# name = input("Nombre: ")
# schoolId = input("Ingresa tu zap: ")
# fromEmail = input("Ingresa tu correo electrónico: ")

# Creamos el objeto "EmailMessage" que sera el contenedor del correo
message = EmailMessage()

# .set_content es para definir el cuerpo del correo
message.set_content(f"soy una cachondita y me gusta el nepe ñam ñam")
message["Subject"] = "Python SMTP"
message["From"] = me
message["To"] = you

"""
Creamos una conexión segura (SSL) con el servidor SMTP de Gmail.

El 'with' se encarga de abrir y cerrar la conexión automáticamente.
La parte 'as smtp' guarda la conexión en la variable 'smtp' para poder usarla dentro del bloque.

Dentro de este bloque:
    - smtp.login(me, app_password) inicia sesión en tu cuenta de Gmail (autenticación).
    - smtp.send_message(message) envía el correo que creamos previamente con EmailMessage.

Cuando el bloque 'with' termina, Python cierra la conexión de forma segura,
incluso si ocurre un error dentro del bloque.
"""
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(me, app_password)
    smtp.send_message(message)

print("Email enviado exitosamente")
