# Guía de Usuario - Automatización de Windows

Este documento proporciona instrucciones sobre cómo configurar y utilizar el sistema de automatización de Windows.

## 1. Configuración Inicial

### 1.1. Instalación de Dependencias

Antes de ejecutar la aplicación, asegúrate de tener Python 3.10+ instalado. Luego, instala las dependencias necesarias ejecutando el siguiente comando en la raíz del proyecto:

```bash
pip install -r requirements.txt
```

### 1.2. Configuración del WebDriver para Control del Navegador (¡Importante!)

Para que las funciones de automatización del navegador (Fase 2) funcionen, necesitas descargar un **WebDriver** que coincida con el navegador que deseas controlar. El WebDriver es el puente entre el script de Python y el navegador.

#### **Instrucciones para Google Chrome:**

1.  **Verifica tu versión de Chrome:**
    *   Abre Chrome, ve al menú de tres puntos (`...`) en la esquina superior derecha.
    *   Ve a `Ayuda` > `Información de Google Chrome`.
    *   Anota la versión (por ejemplo, `125.0.6422.112`).

2.  **Descarga el ChromeDriver correspondiente:**
    *   Visita el [dashboard de descargas de ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/).
    *   Busca la versión que coincida **exactamente** con tu versión de Chrome.
    *   En la sección `stable`, haz clic en la URL correspondiente para descargar el `chromedriver-win64.zip`.

3.  **Configura el ChromeDriver:**
    *   Descomprime el archivo `zip` que descargaste. Dentro encontrarás `chromedriver.exe`.
    *   **Opción A (Recomendado):** Mueve `chromedriver.exe` a una carpeta que esté en el PATH del sistema de Windows (como `C:\Windows\System32` o una carpeta de scripts de Python). Esto permite que el sistema lo encuentre automáticamente.
    *   **Opción B:** Coloca `chromedriver.exe` en la raíz de este proyecto (`windows-automation/`). El script está configurado para buscarlo aquí si no lo encuentra en el PATH.

## 2. Cómo Usar la Aplicación

Ejecuta la aplicación desde la línea de comandos en la raíz del proyecto:

```bash
python main.py
```

### Comandos Disponibles

*   `abre [aplicacion]`: Abre una aplicación predefinida (ej. `abre notepad`).
*   `cierra [aplicacion]`: Cierra una aplicación por su nombre (ej. `cierra notepad`).
*   `salir`: Termina la sesión de la CLI.
