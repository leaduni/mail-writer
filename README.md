
# 📧 Email Sender - LEAD UNI 🚀

Este proyecto permite enviar correos electrónicos personalizados a candidatos de LEAD UNI utilizando un cuerpo de email en HTML y adjuntando imágenes de la marca. Está pensado para facilitar la convocatoria a entrevistas según el pilar correspondiente.✨


## 📝 Instrucciones de uso

1. ✏️ **Modificar el body del email por Pilar**
   - El archivo `body.html` contiene la plantilla del correo. Puedes personalizar el contenido según el pilar (por ejemplo, Excelencia Académica, Liderazgo, etc.).
   - Utiliza los placeholders como `{{nombre}}` y `{{CALENDLY_URL}}` para personalizar cada mensaje.

2. 🔐 **Crear un archivo `.env` y colocar credenciales**
   - Crea un archivo llamado `.env` en la raíz del proyecto.
   - Agrega las siguientes variables con tus credenciales y enlaces:
     ```env
     EMAIL_SMTP_USER=tu_correo@gmail.com
     PASSWORD_SMTP_USER=tu_contraseña
     CALENDLY_URL=tu_link_de_calendly
     ```
   - ⚠️ No compartas este archivo públicamente.

3. 🛠️ **Cambiar los valores del utils**
   - El archivo `utils_data.py` contiene funciones auxiliares, como la obtención de emails por pilar.
   - Puedes modificar este archivo para adaptar la lógica de selección de destinatarios o agregar nuevas funciones según tus necesidades.

## 📂 Estructura del proyecto
- `main.py`: 📨 Script principal para enviar los correos.
- `body.html`: 🖋️ Plantilla HTML del cuerpo del email.
- `utils_data.py`: 🛠️ Funciones auxiliares para manejo de datos.
- `images/`: 🖼️ Carpeta con imágenes usadas en el email.
- `.env`: 🔑 Archivo de variables de entorno (no incluido en el repo).

## ℹ️ Notas
- ✅ Asegúrate de tener las dependencias necesarias instaladas (`smtplib`, `email`, `python-dotenv`).
- 🔒 El envío de correos utiliza SMTP seguro (SSL) con Gmail.
- 📝 Personaliza el asunto y el contenido según el pilar y destinatario.

---

🎯 ¡Listo para convocar a los mejores talentos de LEAD UNI! 🌟
