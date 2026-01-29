# Kermit-DL


#  TERMINAL DE EXTRACCIÓN YOUTUBE v1.0

![Interfaz del Proyecto](https://github.com/xavis3c/Kermit-DL/blob/main/descarga-yt.jpg)

> **ESTADO DEL SISTEMA:** OPERATIVO
> **ENFOQUE:** Ciberseguridad Educativa / Aprendizaje de APIs

Este proyecto es una herramienta de extracción de audio (MP3) de alta velocidad. 
Ha sido diseñado para demostrar cómo interactuar con motores de búsqueda de video (`yt-dlp`) y 
crear puentes de comunicación (Proxies) entre servidores Python y navegadores web.

---

##  ARQUITECTURA DEL SISTEMA

El proyecto está organizado de la siguiente manera para mantener la integridad de los datos:

```text
DESCARGA-YT/

├── templates/          # Almacén de archivos HTML
├── venv/               # Entorno virtual (Cerebro aislado)
├── app.py              # Motor principal (Backend Flask)
├── index.html          # Interfaz de comandos (Frontend)
└── requirements.txt    # Lista de dependencias necesarias

```

---

##  GUÍA DE INSTALACIÓN PARA AGENTES (USUARIOS)

Si eres un usuario nuevo y quieres ejecutar esta terminal en tu computadora, sigue estos pasos:

### 1. Preparar el Terreno (Python).

Asegúrate de tener Python instalado en tu sistema.

* Si usas **Linux Mint/Ubuntu**, abre la terminal y escribe: `sudo apt install python3 python3-pip`.
* Si usas **Windows**, descárgalo desde [python.org](https://python.org).

### 2. Clonar el Repositorio

Descarga este proyecto en tu carpeta preferida.

### 3. Crear el Entorno de Ejecución

Abre una terminal dentro de la carpeta del proyecto y ejecuta estos comandos para crear una "caja de arena" segura (Virtual Environment):

```bash
# Crear entorno
python3 -m venv venv

# Activar el sistema
# En Linux:
source venv/bin/activate
# En Windows:
.\venv\Scripts\activate

```

### 4. Inyectar Dependencias

Instala las librerías necesarias para que el motor funcione:

```bash
pip install -r requirements.txt

```

---

##  MODO DE USO

1. **Encender el Servidor:**
Con el entorno activo, lanza el motor principal:
```bash
python app.py

```


*Deberías ver un mensaje que dice: `Running on http://127.0.0.1:5000*`
2. **Abrir la Interfaz:**
Localiza el archivo `index.html` y ábrelo con tu navegador favorito (Chrome, Firefox o usando Live Server en VS Code).
3. **Ejecutar la Extracción:**
* Pega la URL del video de YouTube en el campo `root@user:~$`.
* Presiona **EJECUTAR**.
* Una vez que el sistema diga `ACCESO CONCEDIDO`, aparecerá el botón: **[ DESCARGAR MP3 ]**.
* Haz clic y espera a que el túnel de datos complete la transferencia a tu carpeta de Descargas.



---

## 🛡️ AVISO DE ÉTICA Y APRENDIZAJE

Este software ha sido creado con fines estrictamente **educativos y de aprendizaje personal**.

* **Investigación:** Se utiliza para entender el funcionamiento de las peticiones HTTP y el manejo de flujos de datos (streams) en Python.
* **Uso Responsable:** No fomentamos la piratería. Utiliza esta herramienta para descargar contenido propio o música con licencias libres (Creative Commons).
* **Seguridad:** El código es abierto para que cualquier estudiante pueda auditarlo y aprender cómo se construye un Proxy de descarga.

---

##  TECNOLOGÍAS UTILIZADAS

* **Python + Flask:** El corazón que procesa las solicitudes.
* **YT-DLP:** El potente motor de extracción de metadatos.
* **Requests:** Para manejar el flujo de datos entre servidores.
* **HTML5 / CSS3 (Matrix Style):** Interfaz visual diseñada para la inmersión.

---

**Desarrollado por un entusiasta de la tecnología para la comunidad de aprendizaje.** 💻🌐
