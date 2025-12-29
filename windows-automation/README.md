# Proyecto de Automatización de Windows

Este proyecto es un sistema de automatización para Windows, controlado mediante comandos de lenguaje natural o a través de una interfaz gráfica (GUI).

## ✨ Características Principales

*   **Interfaz Gráfica de Usuario (GUI):** Una ventana intuitiva para introducir comandos y un editor visual para crear macros.
*   **Procesamiento de Lenguaje Natural (NLP):** Interpreta comandos flexibles y sinónimos.
*   **Gestión de Tareas (Macros):** Crea y ejecuta secuencias de comandos predefinidas.
*   **Gestión Completa de Ventanas y Navegador:** Controla aplicaciones, ventanas y el navegador Chrome.

## 🚀 Cómo Empezar

### Instalación Fácil (Recomendado)

1.  **Ejecuta `install.bat`:** Haz doble clic en el archivo `install.bat`. Este script se encargará de todo: creará un entorno virtual seguro y descargará todas las dependencias necesarias.
2.  **Ejecuta `run.bat`:** Una vez terminada la instalación, haz doble clic en `run.bat` para iniciar la aplicación con su interfaz gráfica.

### Ejecución

*   **Modo Gráfico (GUI):**
    ```bash
    # Si seguiste la instalación fácil
    run.bat

    # O manualmente
    python main.py
    ```
*   **Modo de Línea de Comandos (CLI):**
    ```bash
    python main.py --cli
    ```

## 📦 Compilación a `.exe` (Opcional)

Si deseas distribuir la aplicación como un único archivo ejecutable (`.exe`), puedes compilarla tú mismo.

1.  **Asegúrate de haber instalado las dependencias:** Ejecuta `install.bat` si aún no lo has hecho.
2.  **Ejecuta el script de compilación:**
    ```bash
    python build.py
    ```
3.  **Encuentra el resultado:** El archivo `AsistenteAutomatizacion.exe` aparecerá en una nueva carpeta llamada `dist`.

## 🗺️ Fases del Proyecto (Completadas)

*   **✅ Fases 1-6:** Desarrollo del núcleo, NLP, gestión de tareas y GUI.
*   **✅ Fase 7:** Creación de instaladores (`.bat`) y sistema de compilación (`.exe`).

---
*Este `README.md` ha sido actualizado para reflejar las nuevas capacidades de instalación y distribución.*
