import secrets
import re
import string
from datetime import datetime
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os

def validar_contrasena(password, longitud_minima=10):
    """
    Valida que la contraseña tenga la longitud mínima especificada
    """
    if len(password) < longitud_minima:
        return False, f"❌ La contraseña debe tener al menos {longitud_minima} caracteres"
    
    return True, f"✅ Contraseña válida ({len(password)} caracteres)"

def generar_contrasena():
    """
    Genera una contraseña con variedad de caracteres
    Longitud por defecto: 15 caracteres
    """
    return generar_contrasena_personalizada(15)

def generar_contrasena_personalizada(longitud):
    """
    Genera una contraseña con longitud personalizada
    Incluye mayúsculas, minúsculas, números y símbolos para máxima compatibilidad
    """
    # Caracteres disponibles
    mayusculas = string.ascii_uppercase  # A-Z
    minusculas = string.ascii_lowercase  # a-z
    simbolos = ['*', '+', '-', '/', '@', '_', '?', '!', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#']
    numeros = string.digits  # 0-9

    # Todos los caracteres disponibles
    todos_caracteres = list(mayusculas) + list(minusculas) + simbolos + list(numeros)
    
    # Generar contraseña completamente aleatoria
    contrasena = []
    for i in range(longitud):
        caracter_random = secrets.choice(todos_caracteres)
        contrasena.append(caracter_random)
    
    return "".join(contrasena)


class GeneradorContrasenaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Generador de Contraseñas Flexibles")
        self.root.geometry("600x650")
        self.root.resizable(False, False)
        
        # Variable para la ruta seleccionada
        self.ruta_seleccionada = tk.StringVar()
        self.ruta_seleccionada.set(os.path.join(os.path.expanduser("~"), "Desktop"))  # Escritorio por defecto
        
        self.crear_interfaz()
    
    def crear_interfaz(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Título
        titulo = ttk.Label(main_frame, text="🔐 GENERADOR DE CONTRASEÑAS", 
                          font=("Arial", 16, "bold"))
        titulo.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Información general
        info_frame = ttk.LabelFrame(main_frame, text="ℹ️ Información", padding="10")
        info_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))
        
        info_texto = "• Genera contraseñas con variedad de caracteres\n• Validación únicamente por longitud\n"
        ttk.Label(info_frame, text=info_texto, font=("Arial", 10)).grid(row=0, column=0, sticky=tk.W)
        
        # Configuración de longitud
        config_frame = ttk.LabelFrame(main_frame, text="⚙️ Configuración", padding="10")
        config_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))
        
        ttk.Label(config_frame, text="Longitud de contraseña:").grid(row=0, column=0, sticky=tk.W)
        self.longitud_var = tk.IntVar(value=15)
        longitud_spinbox = ttk.Spinbox(config_frame, from_=10, to=50, width=10, textvariable=self.longitud_var)
        longitud_spinbox.grid(row=0, column=1, padx=(10, 0), sticky=tk.W)
        
        # Selección de ruta
        ruta_frame = ttk.LabelFrame(main_frame, text="📁 Ruta de Guardado", padding="10")
        ruta_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))
        
        ttk.Label(ruta_frame, text="Ruta actual:").grid(row=0, column=0, sticky=tk.W)
        ruta_entry = ttk.Entry(ruta_frame, textvariable=self.ruta_seleccionada, width=50, state="readonly")
        ruta_entry.grid(row=1, column=0, pady=(5, 0), sticky=(tk.W, tk.E))
        
        ttk.Button(ruta_frame, text="📂 Seleccionar Ruta", 
                  command=self.seleccionar_ruta).grid(row=1, column=1, padx=(10, 0), pady=(5, 0))
        
        # Botón generar
        generar_btn = ttk.Button(main_frame, text="🔑 Generar Contraseña", 
                               command=self.generar_y_guardar, style="Accent.TButton")
        generar_btn.grid(row=4, column=0, columnspan=2, pady=(0, 20))
        
        # Resultado
        resultado_frame = ttk.LabelFrame(main_frame, text="🔍 Resultado", padding="10")
        resultado_frame.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))
        
        # Campo de texto para mostrar la contraseña - Ajustado para mostrar todo
        self.resultado_text = tk.Text(resultado_frame, height=12, width=70, wrap=tk.WORD, 
                                     font=("Consolas", 9), state=tk.DISABLED)
        self.resultado_text.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Scrollbar para el texto
        scrollbar = ttk.Scrollbar(resultado_frame, orient=tk.VERTICAL, command=self.resultado_text.yview)
        scrollbar.grid(row=0, column=2, sticky=(tk.N, tk.S))
        self.resultado_text.configure(yscrollcommand=scrollbar.set)
        
        # Configurar el grid para que se expanda
        resultado_frame.columnconfigure(0, weight=1)
        resultado_frame.rowconfigure(0, weight=1)
        
        # Botones adicionales
        botones_frame = ttk.Frame(main_frame)
        botones_frame.grid(row=6, column=0, columnspan=2, pady=(10, 0))
        
        ttk.Button(botones_frame, text="📋 Copiar Contraseña", 
                  command=self.copiar_contrasena).grid(row=0, column=0, padx=(0, 10))
        
        ttk.Button(botones_frame, text="🔄 Nueva Contraseña", 
                  command=self.generar_y_guardar).grid(row=0, column=1, padx=(0, 10))
        
        ttk.Button(botones_frame, text="📂 Abrir Carpeta", 
                  command=self.abrir_carpeta).grid(row=0, column=2)
        
        # Variable para almacenar la última contraseña generada
        self.ultima_contrasena = ""
    
    def seleccionar_ruta(self):
        """Abre un diálogo para seleccionar la carpeta de guardado"""
        ruta = filedialog.askdirectory(
            title="Seleccionar carpeta para guardar la contraseña",
            initialdir=self.ruta_seleccionada.get()
        )
        if ruta:
            self.ruta_seleccionada.set(ruta)
    
    def generar_y_guardar(self):
        """Genera una contraseña y la guarda en la ruta seleccionada"""
        try:
            # Generar contraseña con la longitud especificada
            longitud = self.longitud_var.get()
            contrasena = self.generar_contrasena_personalizada(longitud)
            
            # Validar contraseña (solo longitud)
            longitud_minima = 1  # Mínimo absoluto
            es_valida, mensaje = validar_contrasena(contrasena, longitud_minima)
            
            # Mostrar resultado en la interfaz (sin validación)
            self.mostrar_resultado(contrasena, es_valida, mensaje)
            
            if es_valida:
                # Guardar en archivo
                ruta_archivo = os.path.join(self.ruta_seleccionada.get(), "password.txt")
                self.guardar_contrasena(contrasena, ruta_archivo)
                self.ultima_contrasena = contrasena
                
                # Mensaje de éxito simplificado
                messagebox.showinfo("✅ Éxito", "¡Contraseña lista para usar!")
            else:
                messagebox.showerror("❌ Error", "La contraseña generada no cumple con los requisitos")
                
        except Exception as e:
            messagebox.showerror("❌ Error", f"Error al generar contraseña: {str(e)}")
    
    def generar_contrasena_personalizada(self, longitud):
        """Genera una contraseña con longitud personalizada"""
        return generar_contrasena_personalizada(longitud)
    
    def mostrar_resultado(self, contrasena, es_valida, mensaje):
        """Muestra el resultado en el área de texto"""
        self.resultado_text.config(state=tk.NORMAL)
        self.resultado_text.delete(1.0, tk.END)
        
        # Resultado sin validación
        resultado = f"🔑 CONTRASEÑA GENERADA:\n"
        resultado += f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        resultado += f"Contraseña: {contrasena}\n"
        resultado += f"Longitud: {len(contrasena)} caracteres\n"
        resultado += f"Generada: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        resultado += f"\n📊 CARACTERÍSTICAS:\n"
        resultado += f"• Incluye mayúsculas, minúsculas, números y símbolos\n"
        resultado += f"• Generación completamente aleatoria\n"        
        resultado += f"\n💾 Ruta de guardado:\n{self.ruta_seleccionada.get()}\n"
        resultado += f"\n🔐 ¡Contraseña lista para usar!"
        
        self.resultado_text.insert(1.0, resultado)
        self.resultado_text.config(state=tk.DISABLED)
    
    def guardar_contrasena(self, contrasena, ruta_archivo):
        """Guarda la contraseña en un archivo"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        contenido = "🔐 CONTRASEÑA GENERADA\n"
        contenido += "=" * 50 + "\n"
        contenido += f"Contraseña: {contrasena}\n"
        contenido += f"Longitud: {len(contrasena)} caracteres\n"
        contenido += f"Fecha de generación: {timestamp}\n"
        contenido += "\n📊 CARACTERÍSTICAS:\n"
        contenido += "• Incluye mayúsculas, minúsculas, números y símbolos\n"
        contenido += "• Generación completamente aleatoria\n"        
        
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(contenido)
    
    def copiar_contrasena(self):
        """Copia la última contraseña generada al portapapeles"""
        if self.ultima_contrasena:
            self.root.clipboard_clear()
            self.root.clipboard_append(self.ultima_contrasena)
            messagebox.showinfo("📋 Copiado", "Contraseña copiada al portapapeles")
        else:
            messagebox.showwarning("⚠️ Advertencia", "No hay contraseña para copiar. Genera una primero.")
    
    def abrir_carpeta(self):
        """Abre la carpeta donde se guardan las contraseñas"""
        try:
            if os.name == 'nt':  # Windows
                os.startfile(self.ruta_seleccionada.get())
            elif os.name == 'posix':  # macOS/Linux
                os.system(f'open "{self.ruta_seleccionada.get()}"')
        except Exception as e:
            messagebox.showerror("❌ Error", f"No se pudo abrir la carpeta: {str(e)}")

def main():
    """Función principal - puede ejecutar GUI o consola"""
    import sys
    
    # Si se pasa argumento --console, ejecuta en modo consola
    if len(sys.argv) > 1 and sys.argv[1] == "--console":
        main_consola()
    else:
        # Por defecto, ejecuta la interfaz gráfica
        main_gui()

def main_gui():
    """Ejecuta la interfaz gráfica"""
    root = tk.Tk()
    app = GeneradorContrasenaGUI(root)
    root.mainloop()

def main_consola():
    """Ejecuta en modo consola (función original)"""
    print("🔐 GENERADOR DE CONTRASEÑAS")
    print("=" * 50)
    print("📋 Información:")
    print("• Genera contraseñas con variedad de caracteres")
    print("• Validación únicamente por longitud")    
    print("=" * 50)
    
    # Generar contraseña
    contrasena = generar_contrasena()
    
    # Validar que cumple la longitud mínima
    es_valida, mensaje = validar_contrasena(contrasena, 1)
    
    print(f"\n🔑 Tu nueva contraseña es: {contrasena}")
    print(f"📏 Longitud: {len(contrasena)} caracteres")
    print(f"🔍 Validación: {mensaje}")
    
    if es_valida:
        # Guardar en archivo con información detallada
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open("password.txt", "w", encoding="utf-8") as archivo:
            archivo.write("🔐 CONTRASEÑA GENERADA\n")
            archivo.write("=" * 50 + "\n")
            archivo.write(f"Contraseña: {contrasena}\n")
            archivo.write(f"Longitud: {len(contrasena)} caracteres\n")
            archivo.write(f"Fecha de generación: {timestamp}\n")
            archivo.write("\n📊 CARACTERÍSTICAS:\n")
            archivo.write("• Incluye mayúsculas, minúsculas, números y símbolos\n")
            archivo.write("• Generación completamente aleatoria\n")                        
        
        print(f"💾 Contraseña guardada en 'password.txt'")

    else:
        print("❌ Error: La contraseña generada no cumple")
        print("🔄 Intenta ejecutar el programa nuevamente")


if __name__ == '__main__':
    main()