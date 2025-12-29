import tkinter as tk
from tkinter import scrolledtext, Frame, Label, Entry, Button, Toplevel, messagebox
from src.nlp.command_parser import CommandParser
from src.core import app_manager, browser_manager, window_manager, task_scheduler
from src.utils import config_manager

class SettingsWindow(Toplevel):
    """Ventana emergente para gestionar la configuración de la aplicación."""
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Configuración")
        self.geometry("600x300")
        self.transient(parent)
        self.grab_set()

        self.config_data = config_manager.get_config()

        # --- Sección del LLM ---
        llm_frame = Frame(self, padx=10, pady=10, borderwidth=2, relief="groove")
        llm_frame.pack(fill=tk.X, padx=10, pady=10)

        Label(llm_frame, text="Configuración del LLM", font=("Arial", 14, "bold")).pack(anchor="w")

        # Endpoint
        Label(llm_frame, text="Endpoint URL:", font=("Arial", 10)).pack(anchor="w", pady=(10, 0))
        self.endpoint_entry = Entry(llm_frame, font=("Arial", 10))
        self.endpoint_entry.pack(fill=tk.X)
        self.endpoint_entry.insert(0, self.config_data.get("llm", {}).get("endpoint", ""))

        # Modelo
        Label(llm_frame, text="Modelo:", font=("Arial", 10)).pack(anchor="w", pady=(10, 0))
        self.model_entry = Entry(llm_frame, font=("Arial", 10))
        self.model_entry.pack(fill=tk.X)
        self.model_entry.insert(0, self.config_data.get("llm", {}).get("model", ""))

        # --- Botones de Acción ---
        action_frame = Frame(self)
        action_frame.pack(pady=20)
        Button(action_frame, text="Guardar", command=self.save_settings).pack(side=tk.LEFT, padx=10)
        Button(action_frame, text="Cancelar", command=self.destroy).pack(side=tk.LEFT)

    def save_settings(self):
        # Actualizar el diccionario de configuración
        self.config_data["llm"]["endpoint"] = self.endpoint_entry.get().strip()
        self.config_data["llm"]["model"] = self.model_entry.get().strip()

        if config_manager.save_config(self.config_data):
            messagebox.showinfo("Éxito", "Configuración guardada correctamente.", parent=self)
            self.destroy()
        else:
            messagebox.showerror("Error", "No se pudo guardar la configuración.", parent=self)

class AutomationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Asistente de Automatización")
        # ... (el resto del __init__ se mantiene igual)
        self.parser = CommandParser()
        self.function_map = self._initialize_function_map()
        self._create_widgets()
        self.log_to_output("Bienvenido al Asistente de Automatización.\n")

    def _create_widgets(self):
        top_frame = Frame(self.root)
        top_frame.pack(fill=tk.X, padx=10, pady=5)

        Button(top_frame, text="Crear Tarea", command=self.open_task_editor).pack(side=tk.LEFT)
        Button(top_frame, text="Configuración", command=self.open_settings).pack(side=tk.LEFT, padx=5) # Nuevo botón

        # ... (el resto de los widgets se mantienen igual)
        input_frame = Frame(self.root, pady=5)
        input_frame.pack(fill=tk.X, padx=10)
        Label(input_frame, text="Comando:").pack(side=tk.LEFT)
        self.command_entry = Entry(input_frame, font=("Arial", 12))
        self.command_entry.pack(fill=tk.X, expand=True, side=tk.LEFT, padx=5)
        self.command_entry.bind("<Return>", self.execute_command_event)
        Button(input_frame, text="Ejecutar", command=self.execute_command_event).pack(side=tk.RIGHT)
        self.output_text = scrolledtext.ScrolledText(self.root, state="disabled")
        self.output_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        self.command_entry.focus_set()

    def open_settings(self):
        """Abre la ventana de configuración."""
        SettingsWindow(self.root)

    # ... (El resto de las funciones de AutomationGUI se mantienen igual)
    def execute_command_event(self, event=None):
        command = self.command_entry.get().strip()
        if not command: return

        self.log_to_output(f"> {command}\n")
        self.command_entry.delete(0, tk.END)

        if command.lower() == 'salir':
            browser_manager.cerrar_navegador()
            self.root.quit()
            return

        function_name, entity = self.parser.parse_command(command)

        if function_name and function_name in self.function_map:
            action = self.function_map[function_name]
            if action == "execute_task_flow":
                self.execute_task_flow(entity)
            else:
                self.execute_normal_command(action, entity)
        else:
            self.log_to_output("Comando no reconocido.\n")

    def execute_normal_command(self, action_function, entity):
        try:
            result = action_function(entity) if entity else action_function()
            if result:
                if isinstance(result, list):
                    self.log_to_output("Ventanas abiertas:\n" + "\n".join([f"- {item}" for item in result]) + "\n")
                else:
                    self.log_to_output(f"{result}\n")
        except Exception as e:
            self.log_to_output(f"Error: {e}\n")

    def execute_task_flow(self, task_name):
        self.log_to_output(f"--- Ejecutando Tarea: {task_name} ---\n")
        commands = task_scheduler.get_task_commands(task_name)
        if not commands:
            self.log_to_output(f"Error: Tarea '{task_name}' no encontrada.\n")
            return

        for command in commands:
            self.log_to_output(f"-> {command}\n")
            function_name, entity = self.parser.parse_command(command)
            if function_name and function_name in self.function_map:
                action = self.function_map[function_name]
                if function_name == "ejecutar_tarea":
                    self.log_to_output("Error: No se pueden anidar tareas.\n")
                    continue
                self.execute_normal_command(action, entity)
            else:
                self.log_to_output(f"Comando no reconocido en la tarea: '{command}'\n")
        self.log_to_output(f"--- Tarea '{task_name}' Finalizada ---\n")

    def open_task_editor(self):
        TaskEditorWindow(self.root)

    def log_to_output(self, message):
        self.output_text.config(state="normal")
        self.output_text.insert(tk.END, message)
        self.output_text.see(tk.END)
        self.output_text.config(state="disabled")

    def _initialize_function_map(self):
        return {
            "abrir_aplicacion": app_manager.abrir_aplicacion,
            "cerrar_aplicacion": app_manager.cerrar_aplicacion,
            "navegar_a": browser_manager.navegar_a,
            "buscar_en_google": browser_manager.buscar_en_google,
            "cerrar_navegador": browser_manager.cerrar_navegador,
            "listar_ventanas_abiertas": window_manager.listar_ventanas_abiertas,
            "enfocar_ventana": window_manager.enfocar_ventana,
            "minimizar_ventana": window_manager.minimizar_ventana,
            "maximizar_ventana": window_manager.maximizar_ventana,
            "ejecutar_tarea": "execute_task_flow"
        }

def start_gui():
    root = tk.Tk()
    # Necesitamos una clase TaskEditorWindow para que esto funcione
    # Suponiendo que la definimos en algún lugar, como se mostró anteriormente.
    app = AutomationGUI(root)
    root.mainloop()

if __name__ == '__main__':
    start_gui()
