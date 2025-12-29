import tkinter as tk
from tkinter import scrolledtext, Frame, Label, Entry, Button, Toplevel, messagebox
from src.nlp.command_parser import CommandParser
from src.core import app_manager, browser_manager, window_manager, task_scheduler

class TaskEditorWindow(Toplevel):
    """Ventana emergente para crear y guardar nuevas tareas."""
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Editor de Tareas")
        self.geometry("500x400")
        self.transient(parent) # Mantener esta ventana por encima de la principal
        self.grab_set() # Modal

        # Nombre de la tarea
        Label(self, text="Nombre de la Tarea:", font=("Arial", 12)).pack(pady=(10, 5))
        self.task_name_entry = Entry(self, font=("Arial", 12))
        self.task_name_entry.pack(fill=tk.X, padx=10)

        # Comandos
        Label(self, text="Comandos (uno por línea):", font=("Arial", 12)).pack(pady=(10, 5))
        self.commands_text = scrolledtext.ScrolledText(self, wrap=tk.WORD, font=("Consolas", 10))
        self.commands_text.pack(fill=tk.BOTH, expand=True, padx=10)

        # Botón de Guardar
        Button(self, text="Guardar Tarea", command=self.save_task).pack(pady=10)

    def save_task(self):
        task_name = self.task_name_entry.get().strip()
        commands_raw = self.commands_text.get("1.0", tk.END).strip()

        if not task_name or not commands_raw:
            messagebox.showerror("Error", "El nombre de la tarea y los comandos no pueden estar vacíos.", parent=self)
            return

        commands = [cmd for cmd in commands_raw.split('\n') if cmd.strip()]
        result = task_scheduler.save_new_task(task_name, commands)

        messagebox.showinfo("Resultado", result, parent=self)
        self.destroy()

class AutomationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Asistente de Automatización")
        self.root.geometry("800x600")

        self.parser = CommandParser()
        self.function_map = self._initialize_function_map()

        self._create_widgets()
        self.log_to_output("Bienvenido al Asistente de Automatización.\n")

    def _create_widgets(self):
        top_frame = Frame(self.root)
        top_frame.pack(fill=tk.X, padx=10, pady=5)

        Button(top_frame, text="Crear Tarea", command=self.open_task_editor).pack(side=tk.LEFT)

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
    app = AutomationGUI(root)
    root.mainloop()

if __name__ == '__main__':
    start_gui()
