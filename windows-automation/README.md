# Proyecto de Automatización de Windows

Este proyecto es un sistema de automatización para el sistema operativo Windows, controlado mediante comandos de lenguaje natural o a través de una interfaz gráfica de usuario (GUI). Permite ejecutar tareas repetitivas, gestionar aplicaciones, organizar ventanas y navegar por la web de forma eficiente.

## ✨ Características Principales

El sistema es **completamente funcional** y soporta las siguientes operaciones:

*   **Interfaz Gráfica de Usuario (GUI):**
    *   Una ventana principal intuitiva para introducir comandos y ver los resultados en tiempo real.
    *   Un editor visual para crear y guardar secuencias de comandos (macros) fácilmente.

*   **Procesamiento de Lenguaje Natural (NLP):**
    *   Interpreta comandos flexibles y sinónimos (ej. "inicia notepad" funciona igual que "abre notepad").

*   **Gestión de Tareas (Macros):**
    *   `ejecuta la tarea [nombre]`: Lanza una secuencia de comandos predefinida.
    *   `crea la tarea [nombre]`: Inicia el modo de grabación para definir una nueva macro desde la CLI.

*   **Gestión de Ventanas:**
    *   `lista ventanas`: Muestra todas las ventanas abiertas.
    *   `enfoca`, `minimiza`, `maximiza` una ventana por su título.
    *   `mueve` y `redimensiona` ventanas con coordenadas y tamaños específicos.
    *   `organiza [titulo] en [izquierda/derecha]`: Ajusta una ventana a una mitad de la pantalla.

*   **Control del Navegador Web (Chrome):**
    *   `navega a [url]`: Abre Chrome en la URL especificada.
    *   `busca [termino]`: Realiza una búsqueda en Google.

*   **Gestión de Aplicaciones:**
    *   `abre [aplicacion]`: Inicia aplicaciones comunes (ej. `notepad`, `calculator`).
    *   `cierra [aplicacion]`: Termina procesos de aplicaciones abiertas.

## 🚀 Cómo Empezar

### Prerrequisitos

*   Python 3.10 o superior.
*   El navegador Google Chrome.

### Guía de Instalación

1.  **Clona o descarga el repositorio.**

2.  **Instala las dependencias de Python:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configura el WebDriver (Paso Crucial):**
    Para el control del navegador, es **indispensable** que descargues y configures `chromedriver`. Las instrucciones detalladas se encuentran en la **[Guía de Usuario](docs/user_guide.md)**.

### Ejecución

El programa puede ejecutarse en dos modos:

*   **Modo Gráfico (GUI - Recomendado):**
    ```bash
    python main.py
    ```
    Esto abrirá la ventana principal de la aplicación.

*   **Modo de Línea de Comandos (CLI):**
    ```bash
    python main.py --cli
    ```
    Esto lanzará la versión de texto del asistente.

## 🗺️ Fases del Proyecto (Completadas)

*   **✅ Fase 1: Base del Sistema**
*   **✅ Fase 2: Control de Navegadores**
*   **✅ Fase 3: Gestión Avanzada de Ventanas**
*   **✅ Fase 4: Procesamiento de Lenguaje Natural (NLP)**
*   **✅ Fase 5: Automatización de Tareas (Macros)**
*   **✅ Fase 6: Interfaz Gráfica (GUI)**

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si tienes ideas para nuevas funcionalidades o encuentras algún error, por favor abre un *issue* en el repositorio.
