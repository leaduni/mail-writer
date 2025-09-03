###############
# Email Sender
###############

# HTML Body para el correo electrónico
# Asunto del correo electrónico

# Lista de destinatarios ✅

# Body de HTML ✅

# Links de interés ✅

## Código


from utils.utils_data import get_emails_from_pillar
import smtplib
from email.message import EmailMessage
import ssl
import os
from dotenv import load_dotenv
load_dotenv()

def send_leaduni_invite_html(to_email, pillar_name, nombre_destinatario="Candidato"):
    
    # Leer el HTML
    with open('body.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    html_content = html_content.replace('{{nombre}}', nombre_destinatario)
    html_content = html_content.replace('{{CALENDLY_URL}}', os.getenv('CALENDLY_URL'))
    
    # Crear el mensaje
    msg = EmailMessage()
    msg['Subject'] = f'Invitación a Entrevista - LEAD UNI ({pillar_name}) #2'
    msg['From'] = 'diogo.abregu.g@uni.pe'
    msg['To'] = to_email
    msg.set_content('Para ver este mensaje, habilita la visualización HTML en tu cliente de correo.')
    # Adjuntar HTML
    msg.add_alternative(html_content, subtype='html')

    with open('images/logo-lead-uni.png', 'rb') as img:
        msg.get_payload()[1].add_related(img.read(), 'image', 'png', cid='logo-lead-uni.png')
    with open('images/instagram_dark.png', 'rb') as img:
        msg.get_payload()[1].add_related(img.read(), 'image', 'png', cid='instagram_dark.png')
    with open('images/linkedin.png', 'rb') as img:
        msg.get_payload()[1].add_related(img.read(), 'image', 'png', cid='linkedin.png')
    with open('images/github_dark.png', 'rb') as img:
        msg.get_payload()[1].add_related(img.read(), 'image', 'png', cid='github_dark.png')

    smtp_server = 'smtp.gmail.com'
    smtp_port = 465
    smtp_user = os.getenv('EMAIL_SMTP_USER')
    smtp_pass = os.getenv('PASSWORD_SMTP_USER')
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
        server.login(smtp_user, smtp_pass)
        server.send_message(msg)
    print(f"Correo enviado a {to_email}")
     

# Prueba de envío
if __name__ == "__main__":
    data_students = get_emails_from_pillar(pillar_name='Excelencia Académica')

    for (email, nombre) in data_students:
        send_leaduni_invite_html(email, 'Excelencia Académica', nombre)
