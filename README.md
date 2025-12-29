# Proyecto de Automatización de Windows

Este proyecto es un sistema de automatización para el sistema operativo Windows, diseñado para ser controlado mediante comandos de lenguaje natural. Permite ejecutar tareas repetitivas, gestionar aplicaciones y navegar por la web de forma eficiente, todo desde una simple interfaz de línea de comandos (CLI).

## ✨ Características Actuales

A día de hoy, el sistema es funcional y soporta las siguientes operaciones:

*   **Gestión de Aplicaciones:**
    *   `abre [aplicacion]`: Inicia aplicaciones comunes (ej. `notepad`, `calculator`).
    *   `cierra [aplicacion]`: Termina procesos de aplicaciones abiertas.

*   **Control de Navegador Web (Chrome):**
    *   `navega a [url]`: Abre Google Chrome en la URL especificada (ej. `navega a google.com`).
    *   `busca [termino]`: Realiza una búsqueda en Google con el término indicado.
    *   `cierra navegador`: Cierra la sesión del navegador.

## 🚀 Cómo Empezar

### Prerrequisitos

*   Python 3.10 o superior.
*   El navegador Google Chrome.

### Guía de Instalación

1.  **Clona el repositorio:**
    ```bash
    git clone <URL-DEL-REPOSITORIO>
    cd windows-automation
    ```

2.  **Instala las dependencias de Python:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configura el WebDriver (Paso Crucial):**
    Este proyecto utiliza Selenium para controlar el navegador. Es **indispensable** que descargues y configures `chromedriver`. Las instrucciones detalladas se encuentran en la **[Guía de Usuario](docs/user_guide.md)**.

### Ejecución

Para iniciar la aplicación, ejecuta el siguiente comando desde la carpeta raíz `windows-automation`:

```bash
python main.py
```

Se te presentará una interfaz de línea de comandos donde podrás introducir los comandos.

## 🗺️ Fases del Proyecto

Este proyecto se está desarrollando en fases incrementales:

*   **✅ Fase 1: Base del Sistema:** Configuración del proyecto, CLI básica y gestión de aplicaciones (abrir/cerrar).
*   **✅ Fase 2: Control de Navegadores:** Integración con Selenium para navegación y búsquedas.
*   **▶️ Fase 3: Gestión Avanzada de Ventanas:** Detección, enfoque, movimiento y organización de ventanas.
*   **◻️ Fase 4: Procesamiento de Lenguaje Natural (NLP):** Mejora del reconocimiento de comandos para un lenguaje más flexible.
*   **◻️ Fase 5: Automatización de Tareas (Macros):** Creación y programación de secuencias de comandos.
*   **◻️ Fase 6: Interfaz Gráfica (GUI):** Desarrollo de un panel de control visual para gestionar las tareas.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si tienes ideas para nuevas funcionalidades o encuentras algún error, por favor abre un *issue* en el repositorio.
